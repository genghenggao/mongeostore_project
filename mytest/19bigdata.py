'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-11-20 16:29:21
LastEditors: henggao
LastEditTime: 2020-11-20 21:23:26
'''
# 连接数据库
import time
from bson.json_util import dumps
import pymongo


client = pymongo.MongoClient("192.168.55.110", 20000)
db = client['testdb']
db_coll = db['table1']
# 查询
content = {}
datainfo = []
# print(content)
# print(db_coll.find().count())
start_time = time.time()
# db_coll.find().count()
for document in db_coll.find().limit(200):
    datainfo.append(document)
    content = dumps(datainfo)
# db_coll.find().limit(100000)
print(time.time()-start_time)