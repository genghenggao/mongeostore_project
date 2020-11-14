'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-11-13 15:12:07
LastEditors: henggao
LastEditTime: 2020-11-13 16:15:02
'''
import pymongo
from pymongo import collation
from pymongo import collection
# 连接mongoDB数据库，读取 db 库 table 表中的数据
client = pymongo.MongoClient("192.168.55.110", 20000)
# database = "segyfile"
# db = client[database]
# collection = "excel_data"
# db_coll = db[collection]
# 查询数据库
database_name = client.list_database_names()
if '中文数据库' in database_name:
    print('Wow,数据库存在')
print(database_name) 
# 查询集合
database = client['中文数据库']
collection_name = database.list_collection_names()
print(collection_name)