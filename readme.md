------- ubuntu --------------

sudo apt-get install openssh-server

ln [option] TARGET LINK_NAME

hostname -I

ps aux

kill -9 PID

---------------- MariaDB --------

/opt/google/chrome/google-chrome

f12

apt-get update -y
apt-get install mariadb-server

mysql -V

systemctl status mysql

sudo mysql -u root -p

show databases;

use test;

use tables;

DROP TABLE table_name;

DESC table_name;

SHOW VARIABLES LIKE  'char%';

/etc/mysql/my.cnf

/etc/mysql/mariadb.conf.d/50-serever.cnf
bind-address=0.0.0.0

set sql_mode=''


[client]
default-character-set=utf8

[mysql]
default-character-set=utf8


[mysqld]
collation-server = utf8_unicode_ci
init-connect='SET NAMES utf8'
character-set-server = utf8

CREATE USER 'newuser'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
FLUSH PRIVILEGES;





---------git -----
git -- version
git config --list

git config --global core.autocrlf false

--------------ftp-------------------

sudo apt-get install vsftpd
/etc/vsftpd.conf
anonymous_enable=NO
local_enable=YES
write_enable=YES
chroot_local_user=YES

-------------cron---------------------

crontab -e

sudo systemctl restart cron


-------flask----

from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello, world!'



export FLASK_APP=flaskr
export FLASK_ENV=development
flask run

------------flask(windows10)-------------
set FLASK_APP=flaskr   => export FLASK_APP=flask
set FLASK_ENV=development => export FLASK_ENV=development
flask run   => python -m flask run --host=0.0.0.0





sudo apt-get install mysql-server




sudo systemctl stop apache2

------------linux----------------

adduser username

usermod -aG sudo username

-----------tmux-------------------

tmux
C-b % -> horizontal split

tmux ls
tmux new -s myname
tmux a -t myname

C-b d => detach

INTO OUTFILE '/path/to/file.csv'
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
FROM ts


----------
csv
csv.writer()
.writerow(row)

---------------virtualenv---------------------------
pip install virtualenv

virtualenv --version

virtualenv venv
virtualenv -p /usr/bin/python2.7 env

source venv/bin/activate

deactivate

------ python --------
pip install beautifulsoup4

pip install lxml
sudo -H pip3 install pymysql

--------javascript----------------
XMLHttpRequest()
.onload

.open()
.send(null)

true


