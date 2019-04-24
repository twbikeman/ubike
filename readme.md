mysql -V

systemctl status mysql

mysql -u root -p

show databases;

use test;

use tables;


SHOW VARIABLES LIKE  'char%';

/etc/mysql/my.cnf

[client]
default-character-set=utf8

[mysql]
default-character-set=utf8


[mysqld]
collation-server = utf8_unicode_ci
init-connect='SET NAMES utf8'
character-set-server = utf8

---------------------------------
sudo apt-get install vsftpd
/etc/vsftpd.conf
anonymous_enable=NO
local_enable=YES
write_enable=YES
chroot_local_user=YES

----------------------------------

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
set FLASK_APP=flaskr   => export FLASK_APP=flask
set FLASK_ENV=development => export FLASK_ENV=development
flask run   => python -m flask run --host=0.0.0.0





sudo apt-get install mysql-server


CREATE USER 'newuser'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
FLUSH PRIVILEGES;

sudo systemctl stop apache2

----------------------------

adduser username

tmux
C-b % -> horizontal split

tmux ls

INTO OUTFILE '/path/to/file.csv'
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
FROM ts
----------
csv
csv.writer()
.writerow(row)