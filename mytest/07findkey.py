'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-28 21:26:41
LastEditors: henggao
LastEditTime: 2020-11-05 09:12:19
'''
from gridfs import grid_file
import pymongo
import gridfs
from gridfs import GridFS
from bson import ObjectId
from pymongo.mongo_client import MongoClient
import datetime
client = MongoClient("192.168.55.110", 20000)  # 连接MongoDB数据库
db = client.segyfile  # 选定数据库，设定数据库名称为segyfile
fs = GridFS(db, collection='mysegy')  # 连接GridFS集合，名称为mysegy


print(dir(fs))
print(fs.find_one())
gf = fs.find_one()
print(gf.filename)
print(gf.length)
print(gf.md5)
print(gf.metadata)
print(gf.uploadDate)

print(db.list_collection_names())

print(db.fs.files.find())

gf2 = fs.find()
print("查询"+str(gf2))
list = fs.list
print(list)


# 采用where来，取得id对象的字符串来进行正则匹配
for grid_out in fs.find({"$where": "this._id.match(/.*o/)"}):
    print(grid_out.name)
    print(grid_out.md5)
    print(grid_out)
    print("类型")
    print(type(grid_out))
    # {'_id': 'o_1elnk91eu1dlpbih8qg1vo719tf8', 'filename': '六级成绩单.pdf', 'contentType': 'application/pdf', 'length': 210787, 'uploadDate': datetime.datetime(2020, 10, 28, 12, 52, 44, 702000), 'publisher': 'publisher', 'aliases': ['publisher'], 'metadata': '六级成绩单.pdf', 'md5': 'e3334d50e751a1398c7d1f271c1a21ad', 'chunkSize': 261120}
    print(grid_out._file)


file_sub = fs.find_one(
    {"$where": "this._id.match(/.*o_1em6kn1f71cje1d7r10tjepo18lhk/)"})
print(file_sub.name)
