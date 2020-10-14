'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-14 16:13:54
LastEditors: henggao
LastEditTime: 2020-10-14 16:36:26
'''
from bson import BSON
from pymongo.mongo_client import MongoClient
from gridfs import GridFS

client = MongoClient("192.168.55.110", 20000)
db2 = client.segyfile
filename2 = GridFS(db2, collection="mysegy")

for cursor in filename2.find({"filename": "mytest.SGY"}):
    # print(cursor.filename)
    # print(cursor)
    # content = cursor.read()
    content = b'\xc3@\xf1@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    print(content)
    bosn_obj = BSON(content)
    print(bosn_obj.decode())

##############bson格式字符串#############
    # bson_string = BSON.encode({"hello": "world"})
    # print( bson_string)
    # s = b'\x16\x00\x00\x00\x02hello\x00\x06\x00\x00\x00world\x00\x00'
    # bosn_obj = BSON(s)
    # print(bosn_obj.decode())


# 会出现too large 