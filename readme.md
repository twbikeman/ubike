mysql -V

systemctl status mysql

mysql -u root -p

show databases;

use test;

use tables;

crontab -e

sudo systemctl restart cron

date

select * from  ;


from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello, world!'

export FLASK_APP=flaskr
export FLASK_ENV=development
flask run

------------windows-------------
set FLASK_APP=flaskr
set FLASK_ENV=development
flask run