import os
from flask import Flask
from flask import render_template
from flask import send_file
from flask import Response
import pymysql
import subprocess


try:
    process = subprocess.Popen(['hostname -I'],stdout=subprocess.PIPE, shell=True)
    ipaddr = process.communicate()[0].decode('utf-8','ignore').strip()
    print('ip addr: ', ipaddr)    
except:
    print("fail")



"""
www.cwb.gov.tw/m/o/real/A0A46.html
46693.htm 陽明山 /北投 ZHUZIHU
46691.htm 鞍部 /北投 ANBU
46692.htm 臺北 / 中正 TAIPEI 100
C0AC8.htm 文山 /文山 WENSHAN
C0A98.htm 社子 /士林 SHEZIH
C0A9A.htm 大直 /中山 DAZHI 104
C0A9B.htm 石牌 /北投 SHIPAI
C0A9C.htm 天母 /士林 TIANMU
C0A9E.htm 士林 /士林 SHIHLIN
C0A9F.htm 內湖 /內湖 NEIHU
C0AC7.htm 信義 /信義 XINYI
C0AC4.htm 大屯山 /北投 DATUNSHAN
A0A46.htm 文化大學 /士林 
C0AH4.htm 平等 /士林 PINGDENG
A0A01.htm 臺灣大學 /大安 CONGGUAN
C0AH7.htm 松山 /松山 SONGSHAN
CAAH6.htm 大安森林 /大安
"""

# (sta, '臺北','大直','松山','臺灣大學','大安森林','信義','社子','天母','士林','大屯山','文化大學','平等','陽明山','鞍部','石牌','大屯山','內湖','文山')


# --------------weather--------------------------

db = pymysql.connect(ipaddr,'che0520','che670520','project_dsci')
cursor = db.cursor(pymysql.cursors.DictCursor)
# query_str ="SELECT sta, temp, humid, rain, MAX(time) as time from weather GROUP BY sta;"
query_str ="SELECT sta, temp, humid, rain, MAX(time) as time from weather GROUP BY sta ORDER BY FIELD(sta, '臺北','大直','松山','臺灣大學','大安森林','信義','社子','天母','士林','大屯山','文化大學','平等','陽明山','鞍部','石牌','大屯山','內湖','文山') ;"
cursor.execute(query_str)
weather = {}
db.commit()
for row in cursor:
    sta = row['sta']
    print(row['sta'],row['humid'], row['time'])
    weather[sta] = [row['temp'],row['humid'], row['rain'], row['time']]
db.close()

#--------------------ubike -----------------

db = pymysql.connect(ipaddr,'che0520','che670520','project_dsci')
cursor = db.cursor(pymysql.cursors.DictCursor)
# query_str ="SELECT sta, temp, humid, rain, MAX(time) as time from weather GROUP BY sta;"
query_str ="SELECT sna, tot, sbi, MAX(mday) AS time FROM ubike GROUP BY sno;"
cursor.execute(query_str)
ubike = {}
db.commit()
for row in cursor:
    sna = row['sna']
    demand = int(row['tot']) - int(row['sbi'])
    print(row['sna'],row['tot'], row['sbi'], demand , row['time'])
    ubike[sna] = [int(row['tot']),int(row['sbi']), demand, row['time']]
db.close()

#-------------------------------------------------------------



app = Flask(__name__)



@app.route('/index.html')
def index():
    return render_template('index.html', weather = weather )

@app.route('/queryWeb.html')
def queryWeb():
    return render_template('queryWeb.html', weather = weather)

@app.route('/queryUbike.html')
def queryUbike():
    return render_template('queryUbike.html', ubike = ubike)


@app.route('/datepicker.html')
def datepicker():
    return render_template('datepicker.html')


@app.route( "/<path>")
def DownloadLogFile (path = None):
    try:
        return send_file(path, as_attachment=True)
    except:
        return '404'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 80)


