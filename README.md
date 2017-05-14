** Travel Application **

- How to run this?

1. Setup database
You need to have mysql database.
All database related config is in the file config.py
You need to put root password of mysql in config.py
Run following mysql command to crate database in mysql shell.
```
mysql> create database <DB_NAME>;
```
<DB_NAME> is name of database which you prefer. By default it is `AppDB` set in config.py
Then run following command on Bash shell
```
$ python db.py
```

2. Put application related constants
* Insert FB APP ID
Create FB APP ID from http://developers.facebook.com
Insert it in templates/login.html and in templates/user_page.html

* Insert Google Map API key
Get Google Map API key for your application: https://developers.google.com/maps/documentation/javascript/get-api-key
Search for {GOOGLE_MAPS_API_KEY} in templates/user_page.html and insert your key there.

* Insert Wunderground API Key
Get API key from https://www.wunderground.com/weather/api/d/pricing.html
Wunderground provides weather API
Choose Cumulus plan of API
Insert API key in templates/user_page.html at {WUNDERGROUND_API_KEY}

3. Run Application on localhost
```
$ pip install -r requirements.txt
$ python app.py
```

4. Test this Application
Create test app in FB. There is option to create test app in developers facebook.
Follow: https://developers.facebook.com/docs/apps/test-apps
Create test users to test this test app.

5. Deploy Application
Follow this: http://flask.pocoo.org/docs/0.12/deploying/
