from flask import Flask, render_template, request, session, redirect, \
    url_for, jsonify
from database import db_session
from models import UserData, UserPlace
from sqlalchemy import and_
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
# SECRET_KEY is not important but required.
app.config['SECRET_KEY'] = '04d210d4fd0b48eb4b4a73d165e06598'


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/users', methods=['POST'])
def store_email():
    email = request.json[0]['email']
    name = request.json[0]['name']
    u = UserData.query.filter(UserData.email == email).all()
    session['email'] = email
    if len(u) == 0:
        temp = UserData(name=name, email=email)
        db_session.add(temp)
        db_session.commit()
        temp_u = UserData.query.filter(UserData.email == email).all()
        return str(temp_u[0].id)
    return str(u[0].id)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_home(user_id):
    if 'email' in session:
        u = UserData.query.filter(UserData.id == user_id).all()
        if u[0].email != session['email']:
            return redirect(url_for('login'))
        return render_template('user_page.html',
                               user=str(user_id))
    else:
        return redirect(url_for('login'))


@app.route('/users/<int:user_id>/place', methods=['POST'])
def store_user_entered_placedata(user_id):
    if 'email' in session:
        u = UserData.query.filter(UserData.id == user_id).all()
        if u[0].email != session['email']:
            return redirect(url_for('login'))
        place = request.json[0]['place']
        start_date = request.json[0]['start_date']
        end_date = request.json[0]['end_date']
        try:
            temp = UserPlace(user_id=int(user_id), place=place,
                             start_date=start_date, end_date=end_date)
            db_session.add(temp)
            db_session.commit()
        except IntegrityError:
            db_session.rollback()
        friends = [i['name'] for i in request.json[0]['friends']]
        vfr = db_session.query(UserData.name) \
            .join(UserPlace, UserPlace.user_id == UserData.id) \
            .filter(and_(
                UserData.name.in_(friends), UserPlace.place == place)).all()
        return jsonify(visited_friends=vfr)
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
