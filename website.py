import os
from flask import Flask, request
from flask import render_template
from flask import send_file
from flask import Response
import pymysql

import datetime




#---------------global--------------

class Data:
    def __init__(self):
        self.listData = []
        self.dictData = {}
        self.sta = ''
        self.date = datetime.datetime.now()
        

current = Data()
print(current.listData)


def convArea(sta):
    switcher = {
        '陽明山': '北投',
        '鞍部': '北投',
        '臺北': '中正',
        '文山': '文山',
        '社子': '士林',
        '大直': '中山',
        '石牌': '北投',
        '天母': '士林',
        '士林': '士林',
        '內湖': '內湖',
        '信義': '信義',
        '大屯山': '北投',
        '文化大學': '士林', 
        '平等': '士林',
        '臺灣大學': '大安',
        '松山': '松山',
        '大安森林': '大安'
    }
    return switcher.get(sta,'invalid')



#---------- weather query function ----------------------
def queryWeather(query_str):
    db = pymysql.connect('127.0.0.1','che0520','che670520','project_dsci')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query_str)
    weather = []
    db.commit()
    for row in cursor:
        sta = row['sta']
        weather[sta] = [row['temp'],row['humid'], row['rain'], row['time']]
    db.close()
    return weather

# --------------weather--------------------------
def getLastestWeather():
    db = pymysql.connect('127.0.0.1','che0520','che670520','project_dsci')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    query_str ="SELECT weather.sta, temp, humid, rain, time FROM weather INNER JOIN (SELECT sta, MAX(time) AS maxtime FROM weather GROUP BY sta) AS latest On (weather.sta = latest.sta AND latest.maxtime = weather.time) ORDER BY FIELD (weather.sta, '臺北','大直','松山','臺灣大學','大安森林','信義','社子','天母','士林','大屯山','文化大學','平等','陽明山','鞍部','石牌','大屯山','內湖','文山');"
    cursor.execute(query_str)
    weather = []
    db.commit()
    for row in cursor:
        weather.append([row['sta'],row['temp'], row['humid'], row['rain'], row['time'], convArea(row['sta'])])
    db.close()
    return weather

#-------------ubike---------------------

def getUbikeData(query_str):
    db = pymysql.connect('127.0.0.1','che0520','che670520','project_dsci')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query_str)
    ubike = []
    db.commit()
    for row in cursor:
        time = row['time'].strftime('%H:%M')
        demand = row['tot'] - row['sbi']
        tot = row['tot']
        ubike.append([time, demand, tot])
    db.close()
    return ubike


#--------------------ubike -----------------
def getLastestUbike():
    db = pymysql.connect('127.0.0.1','che0520','che670520','project_dsci')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    
    query_str ="SELECT ubike.sna, ubike.tot, ubike.sbi, ubike.mday FROM ubike INNER JOIN (SELECT sna, MAX(mday) AS mtime FROM ubike GROUP BY sna) AS latest ON (ubike.sna = latest.sna AND ubike.mday = latest.mtime);"

    cursor.execute(query_str)
    ubike = []
    db.commit()
    for row in cursor:
        sna = row['sna']
        demand = int(row['tot']) - int(row['sbi'])
        ubike.append([sna, row['tot'], row['sbi'], demand, row['mday']])
    db.close()
    return ubike

#-------------------------------------------------------------



app = Flask(__name__)




@app.route('/')
def root():
    return render_template('index.html', pieData = [11,22,33])



@app.route('/pie4.html')
def pie4():
    return render_template('pie4.html', pieData = [11,22,33])



@app.route('/queryWeb.html')
def queryWeb():
    weather = getLastestWeather()
    return render_template('queryWeb.html', weather = weather)

@app.route('/queryUbike.html')
def queryUbike():
    ubike = getLastestUbike()
    return render_template('queryUbike.html', ubike = ubike)



## make json file

@app.route('/getUbike.html', methods = ['POST']) 
def getUbike():
    if request.method == 'POST':

        query_str =  "SELECT sna, tot, sbi, mday AS time From ubike WHERE sna = '{}' AND DATE(mday) = '{}' ".format(request.form['sta'], request.form['ubikeDate'])
        bike = getUbikeData(query_str)
        tot = bike[0][2]
        
        with open("templates/data/dataUbike.json","w") as fp:
            newList=[]
            
            for row in bike:
                newList.append('"{}":{}'.format(row[0], row[1]))
            fp.write('{')
            fp.write('{}'.format(','.join(newList)))
            fp.write('}')
            
        ## update the content
        return str(tot)
        # return request.form['sta'] + request.form['_date'] 








@app.route( "/data/<path>")
def data(path):
    return render_template('/data/' + path)





if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 80, debug = True)


