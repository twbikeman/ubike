import json
import pymysql
import requests

url = 'http://data.taipei/youbike'

data = requests.get(url)
# data.encoding = 'utf-8'
# print(data.content.decode('utf-8'))
data = json.loads(data.content.decode('utf-8'))
# for i in data['retVal'].keys():
#     print('sno: ', data['retVal'][i]['sno'])
#     print('sna: ', data['retVal'][i]['sna'])
#     print('tot: ', data['retVal'][i]['tot'])
#     print('sbi: ', data['retVal'][i]['sbi'])
#     print('bemp', data['retVal'][i]['bemp'])
#     print('act', data['retVal'][i]['act'])
#     print('--------------------------------')

#http://data.taipei/youbike

# sno：站點代號、 sna：場站名稱(中文)、 tot：場站總停車格、 sbi：場站目前車輛數量、 sarea：場站區域(中文)、 mday：資料更新時間、 lat：緯度、 lng：經度、 ar：地(中文)、 sareaen：場站區域(英文)、 snaen：場站名稱(英文)、 aren：地址(英文)、 bemp：空位數量、 act：全站禁用狀態


# {"retCode":1,"retVal":{"0001":{"sno": "0001", "sna": "捷運市政府站(3號出口)", "tot": "180", "sbi": "139", "sarea": "信義區", "mday": "20190412152034", "lat": "25.0408578889", "lng": "121.567904444", "ar": "忠孝東路/松仁路(東南側)", "sareaen": "Xinyi Dist.", "snaen": "MRT Taipei City Hall Stataion(Exit 3)-2", "aren": "The S.W. side of Road Zhongxiao East Road & Road Chung Yan.", "bemp": "40", "act": "1"},


db = pymysql.connect('192.168.11.11','root','che670520','test')
cursor = db.cursor()
str1 ="INSERT INTO ubike(sno, tot, sbi) VALUES('{0}','{1}','{2}')"
line = 0
for i in data['retVal'].keys():
    sno = data['retVal'][i]['sno']
    tot = data['retVal'][i]['tot']
    sbi = data['retVal'][i]['sbi']
    cursor.execute(str1.format(sno, tot, sbi))
    db.commit()
    line +=1
db.close()

# with open('YouBikeTP.gz','r', encoding='utf-8',errors='ignore') as filePt:
#     data = json.load(filePt)
#     # print(data['retVal']['0001'])
#     for i in data['retVal'].keys():
#         print('sno: ', data['retVal'][i]['sno'])
#         print('sna: ', data['retVal'][i]['sna'])
#         print('tot: ', data['retVal'][i]['tot'])
#         print('sbi: ', data['retVal'][i]['sbi'])
#         print('bemp', data['retVal'][i]['bemp'])
#         print('act', data['retVal'][i]['act'])
#         print('--------------------------------')




# .sql
# CREATE DATABASE project_dsci;
# CREATE TABEL ubike (
#     id INT NOT NULL AUTO_INCREMENT,
#     sno VARCHAR(40),
#     sna VARCHAR(40),
#     tot INT,
#     sbi INT,
#     sarea VARCHAR(40),
#     mday TIMESTAMP;
#     lat FLOAT;
#     lng FLOAT;
#     sareaen VARCHAR(40),
#     snaen VARCHAR(40,)
#     aren VARCHAR(40),
#     bemp INT,
#     act INT
# );

#sno：站點代號、 sna：場站名稱(中文)、 tot：場站總停車格、 sbi：場站目前車輛數量、 sarea：場站區域(中文)、 mday：資料更新時間、 lat：緯度、 lng：經度、 ar：地(中文)、 sareaen：場站區域(英文)、 snaen：場站名稱(英文)、 aren：地址(英文)、 bemp：空位數量、 act：全站禁用狀態