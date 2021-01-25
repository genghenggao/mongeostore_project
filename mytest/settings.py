'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2021-01-20 15:29:44
LastEditors: henggao
LastEditTime: 2021-01-21 10:33:52
'''
## MongoDB数据库设置 ##
import pymongo
MongoDB_client = pymongo.MongoClient("192.168.55.110", 20000)

### MongoDB Atlas ###
# MONGODB_URL = "mongodb+srv://henggao:tel123456@mongeostore.tgjjd.mongodb.net/mongoestore?retryWrites=true&w=majority"
MONGODB_URL = "mongodb+srv://henggao:tel123456@mongeostore.tgjjd.mongodb.net"
MongoDB_Atlas_client = pymongo.MongoClient(MONGODB_URL)

### mongoengine 连接Atlas ###
MONGODB_Atlas_URL = "mongodb+srv://henggao:tel123456@mongeostore.tgjjd.mongodb.net"