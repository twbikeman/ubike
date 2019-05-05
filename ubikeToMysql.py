import json
import pymysql
import requests
import subprocess


try:
    process = subprocess.Popen(['hostname -I'],stdout=subprocess.PIPE, shell=True)
    ipaddr = process.communicate()[0].decode('utf-8','ignore').strip()
    print('ip addr: ', ipaddr)    
except:
    print("fail")

#http://data.taipei/youbike

url = 'http://data.taipei/youbike'
data = requests.get(url)

# print(data.content.decode('utf-8'))

data = json.loads(data.content.decode('utf-8'))
db = pymysql.connect(ipaddr,'che0520','che670520','project_dsci')


for i in data['retVal'].keys():
    print('--------------------------------')
    print('sno: ', data['retVal'][i]['sno'])
    print('sna: ', data['retVal'][i]['sna'])
    print('tot: ', data['retVal'][i]['tot'])
    print('sbi: ', data['retVal'][i]['sbi'])
    print('sarea: ', data['retVal'][i]['sarea'])
    print('mday: ', data['retVal'][i]['mday'])
    print('lat: ', data['retVal'][i]['lat'])
    print('lng: ', data['retVal'][i]['lng'])
    print('sareaen: ', data['retVal'][i]['sareaen'])
    print('snaen: ', data['retVal'][i]['snaen'])
    print('ar: ', data['retVal'][i]['ar'])
    print('aren: ', data['retVal'][i]['aren'])
    print('bemp', data['retVal'][i]['bemp'])
    print('act', data['retVal'][i]['act'])
   







# mysql here #


cursor = db.cursor()
str1 ="INSERT INTO ubike(sno, sna, tot, sbi, sarea, mday, lat, lng, sareaen, snaen, ar, aren, bemp, act) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"
line = 0
for i in data['retVal'].keys():
    sno = data['retVal'][i]['sno']
    sna = data['retVal'][i]['sna']
    tot = data['retVal'][i]['tot']
    sbi = data['retVal'][i]['sbi']
    sarea = data['retVal'][i]['sarea']
    mday = data['retVal'][i]['mday']
    lat = data['retVal'][i]['lat']
    lng = data['retVal'][i]['lng']
    sareaen = data['retVal'][i]['sareaen']
    snaen = data['retVal'][i]['snaen'].replace('&','').replace("'",'')
    ar = data['retVal'][i]['ar'].replace('&','').replace("'",'')
    aren = data['retVal'][i]['aren'].replace('&','').replace("'",'')
    bemp = data['retVal'][i]['bemp']
    act = data['retVal'][i]['act']
    cursor.execute(str1.format(sno, sna, tot, sbi, sarea, mday, lat, lng, sareaen, snaen, ar, aren, bemp, act))
    
    db.commit()
    line +=1
db.close()

