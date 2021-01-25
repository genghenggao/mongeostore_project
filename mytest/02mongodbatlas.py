'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2021-01-20 09:06:06
LastEditors: henggao
LastEditTime: 2021-01-21 11:09:46
'''
#!/usr/bin/python3
# coding=utf-8
# import pymongo
# import urllib
# from urllib import parse

# mongo_uri = 'mongodb+srv://henggao:tel123456@cluster0-nnssa.mongodb.net/test?retryWrites=true&w=majority'
# mongo_uri = 'mongodb+srv://henggao:tel123456@mongeostore.tgjjd.mongodb.net/mongeostore?retryWrites=true&w=majority'
# mongo_uri = 'mongodb+srv://henggao:@Tell5351818127@mongeostore.tgjjd.mongodb.net/mongeostore?retryWrites=true&w=majority'
# 转义用户名和密码
# mongo_uri = 'mongodb+srv://henggao:' + urllib.parse.quote(
#     '@Tel15351818127') + '@mongeostore-tgjjd.mongodb.net/mongeostore?retryWrites=true&w=majority'

# myclient = pymongo.MongoClient(mongo_uri)
# dblist = myclient.list_database_names()
# print(dblist)
# if "gridfs" in dblist:
#     print("数据库已存在！")


# client = pymongo.MongoClient("mongodb+srv://henggao:tel123456@mongeostore.tgjjd.mongodb.net/mongeostore?retryWrites=true&w=majority")
# db = client.test

# print(db)


import pymongo
from pymongo import MongoClient
import urllib.parse
import settings

# username = urllib.parse.quote_plus('henggao')
# password = urllib.parse.quote_plus("tel123456")

# url = "mongodb+srv://henggao:<password>@mongeostore.tgjjd.mongodb.net/<dbname>?retryWrites=true&w=majority".format(username, password)
# url = "mongodb+srv://henggao:tel123456@mongeostore.tgjjd.mongodb.net/mongoestore?retryWrites=true&w=majority"
url = "mongodb+srv://henggao:tel123456@mongeostore.tgjjd.mongodb.net"
# url is just an example (your url will be different)

cluster = MongoClient(url)
db = cluster['demo01']
collection = db['test01']

### Demo1 插入数据 #######
# data = {
#     "mobile": 15518501828,
#     "code": 123456,
# }
# collection.insert_one(document=data)

# print(db)
# print(collection)


### Demo2 查询数据库 #######
# dblist = cluster.list_database_names()
# print(dblist)


###    使用配置文件连接MongoDB （当前目录下settings.py）     ###
# client = settings.MongoDB_client   
# client = settings.MongoDB_Atlas_client
# # dblist = client.list_database_names()
# # print(dblist)
# db  = client['钻孔数据管理子系统']
# collection = db['定位表']
# # print(db)
# print(collection)



# client = MongoClient("192.168.55.110", 27017)
client = MongoClient("192.168.55.110:27017")
db  = client['钻孔数据管理子系统']
collection = db['定位表']
print(db)
print(collection)