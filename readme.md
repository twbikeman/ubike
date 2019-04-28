------- ubuntu --------------

sudo apt-get install openssh-server

ln [option] TARGET LINK_NAME

hostname -I

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


SHOW VARIABLES LIKE  'char%';

/etc/mysql/my.cnf

/etc/mysql/mariadb.conf.d/50-serever.cnf
bind-address=0.0.0.0

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

# CREATE DATABASE project_dsci;
CREATE TABLE ubike (
     id INT NOT NULL AUTO_INCREMENT,
     sno VARCHAR(10),
     sna VARCHAR(40),
     tot INT,
     sbi INT,
     sarea VARCHAR(40),
     mday TIMESTAMP,
     lat FLOAT,
     lng FLOAT,
     ar VARCHAR(40),
     sareaen VARCHAR(40),
     snaen VARCHAR(40,)
     aren VARCHAR(40),
    bemp INT,
     act INT,
);

# {"retCode":1,"retVal":{"0001":{"sno": "0001", "sna": "捷運市政府站(3號出口)", "tot": "180", "sbi": "139", "sarea": "信義區", "mday": "20190412152034", "lat": "25.0408578889", "lng": "121.567904444", "ar": "忠孝東路/松仁路(東南側)", "sareaen": "Xinyi Dist.", "snaen": "MRT Taipei City Hall Stataion(Exit 3)-2", "aren": "The S.W. side of Road Zhongxiao East Road & Road Chung Yan.", "bemp": "40", "act": "1"},


---------git -----
git -- version
git config --list
.git/config
git config --global core.autocrlf false
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




sudo systemctl stop apache2

----------------------------

adduser username

usermod -aG sudo username

------------------------------inpu

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

------------------------------------------
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