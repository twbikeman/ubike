import os
from flask import Flask, request
from flask import render_template
from flask import send_file
from flask import Response
import pymysql
import subprocess
import datetime

try:
    process = subprocess.Popen(['hostname -I'],stdout=subprocess.PIPE, shell=True)
    ipaddr = process.communicate()[0].decode('utf-8','ignore').strip()
    print('ip addr: ', ipaddr)    
except:
    print("fail")

#---------------global--------------

class Data:
    def __init__(self):
        listData = []
        dictData = {}
        sta = ''
        date = datetime.datetime.now()
        

current = Data()

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


#---------- weather query function ----------------------
def query_weather(query_str):
    db = pymysql.connect(ipaddr,'che0520','che670520','project_dsci')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # query_str ="SELECT sta, temp, humid, rain, MAX(time) as time from weather GROUP BY sta;"
    # query_str ="SELECT sta, temp, humid, rain, MAX(time) as time from weather GROUP BY sta ORDER BY FIELD(sta, '臺北','大直','松山','臺灣大學','大安森林','信義','社子','天母','士林','大屯山','文化大學','平等','陽明山','鞍部','石牌','大屯山','內湖','文山') ;"
    cursor.execute(query_str)
    weather = {}
    db.commit()
    for row in cursor:
        sta = row['sta']
        print(row['sta'],row['humid'], row['time'])
        weather[sta] = [row['temp'],row['humid'], row['rain'], row['time']]
    db.close()
    return weather

# --------------weather--------------------------
def getLastestWeather():
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
    return weather

#-------------ubike---------------------

def getUbikeData(query_str="SELECT sna, tot, sbi, MAX(mday) AS time FROM ubike GROUP BY sno;"):
    db = pymysql.connect(ipaddr,'che0520','che670520','project_dsci')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # query_str ="SELECT sta, temp, humid, rain, MAX(time) as time from weather GROUP BY sta;"
    cursor.execute(query_str)
    ubike = {}
    db.commit()
    for row in cursor:
        time = row['time']
        demand = int(row['tot']) - int(row['sbi'])
        print(row['time'], row['sna'],row['tot'], row['sbi'], demand )
        ubike[time] = [row['sna'],int(row['tot']),int(row['sbi']), demand]
    db.close()
    return ubike, row['sna'], row['time']


#--------------------ubike -----------------
def getLastestUbike():
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
    return ubike

#-------------------------------------------------------------



app = Flask(__name__)



@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/hello.html')
def hello():
    return render_template('hello.html')

@app.route('/pie3.html')
def pie():
    return render_template('pie3.html')

@app.route('/pie4.html')
def pie4():
    return render_template('pie4.html', data = {'a':11,'b':22})

@app.route('/bar3.html')
def bar3():
    # global gData
    # print(gData)
    return render_template('bar3.html', data = current.listData)
# [5, 10, 13, 19, 21, 25, 22, 18, 15, 13, 11, 12, 15, 20, 18, 17, 16, 18, 23, 25, 11, 11, 11] 
    


@app.route('/queryWeb.html')
def queryWeb():
    weather = getLastestWeather()
    return render_template('queryWeb.html', weather = weather)

@app.route('/queryUbike.html')
def queryUbike():
    ubike = getLastestUbike()
    return render_template('queryUbike.html', ubike = ubike)




@app.route('/getUbike.html', methods = ['GET','POST'])
def getUbike():
    if request.method == 'GET':
        return request.args.get('query')
    if request.method == 'POST':

        query_str =  'SELECT sna, tot, sbi, mday AS time From ubike WHERE sna = ' + '"' + request.form['sta'] + '" '  \
            +  'AND DATE(mday) = ' + '"' + request.form['date'] + '";'
        print(query_str)
        bike, current.sta, current.date = getUbikeData(query_str)
        print(bool(bike))
        print(bike)
        bike_demand = []
        for key, value in bike.items():
            bike_demand.append(value[3])
        # print(bike_demand)
        # global gData
        # gData = bike_demand[:]
        current.listData = bike_demand[:]
        print("----query data-----")
        print(current.listData)
        print(current.date)
        print(current.sta)
        return request.form['sta'] + request.form['date']




@app.route('/queryOneUbike.html')
def queryOneUbike():
    return render_template('queryOneUbike.html')

@app.route('/webAfterQuery.html')
def webAfterQuery():
    myweather = query_weather("SELECT sta, temp, humid, rain, time from weather WHERE time >= '2019-05-11 01:00:00' AND time <= '2019-05-11 02:00:00';")
    print(myweather)
    return render_template('webAfterQuery.html', weather = myweather)

@app.route( "/data/<path>")
def data(path):
    return render_template('/data/' + path)



@app.route( "/<path>")
def DownloadLogFile (path = None):
    try:
        return send_file(path, as_attachment=True)
    except:
        return '404'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 80, debug = True)


