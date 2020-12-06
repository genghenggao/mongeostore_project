'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-12-06 18:30:07
LastEditors: henggao
LastEditTime: 2020-12-06 22:06:35
'''
from bson.son import SON
from pymongo import MongoClient, GEO2D

# 使用geo_example库
# db = MongoClient("192.168.55.110", 20000).geo_example
# # 创建索引在places上的loc列
# db.places.create_index([("loc", GEO2D)])
# db.places.ensure_index([("loc", GEO2D)])
# 插入坐标数据
# result = db.places.insert_many(
#     [{"loc": [2, 5]}, {"loc": [30, 5]}, {"loc": [1, 2]}, {"loc": [4, 4]}])

# 查询离［3，6］最近的坐标
# for doc in db.places.find({"loc": {"$near": [3, 6]}}).limit(3):
#     repr(doc)
#     # print(repr(doc))
#     print(doc)

# # 增加最大距离
# query = {"loc": SON([("$near", [3, 6]), ("$maxDistance", 2)])}

# # 在（2，2） （5，6）lower-left and upper-right
# query = {"loc": {"$geoWithin": {"$box": [[2, 2], [5, 6]]}}}
# for doc in db.places.find(query).sort('_id'):
#     repr(doc)
#     # print(repr(doc))
#     print(doc)
# # 在半径为6的圆内
# query = {"loc": {"$geoWithin": {"$center": [[0, 0], 6]}}}
# for doc in db.places.find(query).sort('_id'):
#     repr(doc)
#     print(doc)


# db.command(SON([('geoNear', 'places'), ('near', [1, 2])]))


client = MongoClient("192.168.55.110", 20000)
db = client['钻孔数据管理子系统']
col = db['GeoJSON']
col.create_index([("coordinates", GEO2D)])

for doc in col.find({"locaton.coordinates": {"$near": [138.25947, 59.913501]}}).limit(3):
    repr(doc)
    # print(repr(doc))
    print(doc)
# for doc in db.places.find(query).sort('_id'):
#     print(doc)
