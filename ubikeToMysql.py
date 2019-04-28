import json
import pymysql
import requests

#http://data.taipei/youbike

url = 'http://data.taipei/youbike'
data = requests.get(url)

# print(data.content.decode('utf-8'))

data = json.loads(data.content.decode('utf-8'))


# {"retCode":1,"retVal":{"0001":{"sno": "0001", "sna": "捷運市政府站(3號出口)", "tot": "180", "sbi": "139", "sarea": "信義區", "mday": "20190412152034", "lat": "25.0408578889", "lng": "121.567904444", "ar": "忠孝東路/松仁路(東南側)", "sareaen": "Xinyi Dist.", "snaen": "MRT Taipei City Hall Stataion(Exit 3)-2", "aren": "The S.W. side of Road Zhongxiao East Road & Road Chung Yan.", "bemp": "40", "act": "1"},

# sno：站點代號、 sna：場站名稱(中文)、 tot：場站總停車格、 sbi：場站目前車輛數量、 sarea：場站區域(中文)、 mday：資料更新時間、 lat：緯度、 lng：經度、 ar：地(中文)、 sareaen：場站區域(英文)、 snaen：場站名稱(英文)、 aren：地址(英文)、 bemp：空位數量、 act：全站禁用狀態

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

# db = pymysql.connect('192.168.11.11','root','che670520','test')
# cursor = db.cursor()
# str1 ="INSERT INTO ubike(sno, tot, sbi) VALUES('{0}','{1}','{2}')"
# line = 0
# for i in data['retVal'].keys():
#     sno = data['retVal'][i]['sno']
#     tot = data['retVal'][i]['tot']
#     sbi = data['retVal'][i]['sbi']
#     cursor.execute(str1.format(sno, tot, sbi))
#     db.commit()
#     line +=1
# db.close()

