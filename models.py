from sqlalchemy import Column, Integer, String, Date, UniqueConstraint
from database import Base


class UserData(Base):
    __tablename__ = 'user_data'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)


class UserPlace(Base):
    __tablename__ = 'user_places'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    place = Column(String(120), unique=False)
    start_date = Column(Date)
    end_date = Column(Date)

    __table_args__ = (
        UniqueConstraint('user_id', 'place', 'start_date', 'end_date'),)

    def __init__(self, user_id=None, place=None,
                 start_date=None, end_date=None):
        self.place = place
        self.user_id = user_id
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return '<User %r is going to %r>' % (self.id, self.place)
