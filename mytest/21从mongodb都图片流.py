'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-11-27 11:13:50
LastEditors: henggao
LastEditTime: 2020-11-27 14:27:24
'''
from pymongo import MongoClient
from gridfs import GridFS

client = MongoClient("192.168.55.110", 20000)
db = client.segyfile  # 选定数据库，设定数据库名称为segyfile
fs = GridFS(db, collection='mysegy')  # 连接GridFS集合，名称为mysegy

