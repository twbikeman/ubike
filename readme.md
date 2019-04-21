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


CREATE USER 'newuser'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
FLUSH PRIVILEGES;

sudo systemctl stop apache2

tmux
C-b % -> horizontal split

tmux ls

INTO OUTFILE '/path/to/file.csv'
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
FROM ts

csv
csv.writer()

.writerow(row)