'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-11 16:39:26
LastEditors: henggao
LastEditTime: 2020-10-11 19:19:40
'''
import pymongo
from pymongo import MongoClient

######example 查询数据库下所有collection名称########
client = MongoClient("192.168.55.110", 20000)
db = client['gridfs']
coll_names = db.list_collection_names(session=None)
print(coll_names)   #['LX_SEGY', 'LX_SEGY2', 'fs.files', 'fs.chunks', 'User']

# fs = client.gridfs.User
# print(fs.find_one({"id":1}))  #{'_id': ObjectId('5e133e80ed7ea23fbc8c97f5'), 'id': 1.0, 'username': 'henggao', 'password': 123456.0}
fs = client.gridfs.LX_SEGY
print(fs.find_one({"trace":0})) #{'_id': ObjectId('5e0b4e2d882821b35c62b442'), 'trace': 0, 'sample': 0, 'value': 0.0}
print(fs.find_one({"_id":"5e0b4e2d882821b35c62b442"})) # None
print(fs.find_one({"Objectid":"5e0b4e2d882821b35c62b442"})) # None
print(fs.find_one({'_id': "ObjectId('5e0b4e2d882821b35c62b442')"})) # None

from bson import ObjectId
print(fs.find_one({'_id': ObjectId('5e0b4e2d882821b35c62b442')})) # {'_id': ObjectId('5e0b4e2d882821b35c62b442'), 'trace': 0, 'sample': 0, 'value': 0.0}
# 原来ObjectId是一个对象，而不是一个字符串

#从第几行开始读取(SLICE)，读取多少行(LIMIT)
for u in fs.find().skip(2).limit(3): 
    print (u)
    
######使用segyio读取segy文件
import segyio
# print()filename
# with segyio.open(filename,mode="r",strict=False,ignore_geometry=False, endian='big') as f:
#     print(f.tracecount)
