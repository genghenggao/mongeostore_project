'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-12-14 17:43:04
LastEditors: henggao
LastEditTime: 2020-12-14 19:55:07
'''
import random
from pymongo import MongoClient

client = MongoClient("192.168.55.110", 20000)
mydb = client['钻孔数据管理子系统']
mycol = mydb['定位表']


Lng_A = 102
Lng_B = 109
C = 5  # 设置精度
Lat_A = 28
Lat_B = 35
i = 1
while i < 100:
    Lng = random.uniform(Lng_A, Lng_B)
    Lat = random.uniform(Lat_A, Lat_B)
    Depth = random.uniform(260, 400)
    coor_E = random.uniform(2000, 2240)
    coor_N = random.uniform(4700, 5200)
    coor_R = random.uniform(260, 320)
    lng = round(Lng, C)
    lat = round(Lat, C)
    depth = round(Depth, 3)
    coordinate_E = round(coor_E, 3)
    coordinate_N = round(coor_N, 3)
    coordinate_R = round(coor_R, 3)

    # zknum = random.randint(1, 20)

    # print([lng, lat, i])
    zknum = 'ZK' + str(i)
    jsondata = {
        'zk_name': zknum,
        'coordinate_E': coordinate_E,
        'coordinate_N': coordinate_N,
        'coordinate_R': coordinate_R,
        'max_depth': depth,
        'track_type': '曲',
        'location': {
            'type': "Point",
            "coordinates": [lng, lat]
        },
    }
    i += 1

    # drilllocation = {}
    # drilllocation.push(jsondata)
    mycol.insert_one(jsondata)
    print(jsondata)
