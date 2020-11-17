'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-11-13 15:12:07
LastEditors: henggao
LastEditTime: 2020-11-17 19:59:08
'''
import re
from re import match
import pymongo
from pymongo import collection
# 连接mongoDB数据库，读取 db 库 table 表中的数据
client = pymongo.MongoClient("192.168.55.110", 20000)
# database = "segyfile"
# db = client[database]
# collection = "excel_data"
# db_coll = db[collection]
# 查询数据库
databases = client.list_database_names()
# if '中文数据库' in databases:
#     print('Wow,数据库存在')
print(databases)
# 查询集合
# database = client['中文数据库']
# collection_name = database.list_collection_names()
# print(collection_name)
# 去掉admin与config数据库
databases.remove('admin')
databases.remove('config')
print(databases)
print(len(databases))
database_total = len(databases)  # 获取数据库个数

# print("=========================================")
list_db = []
# children = []
dict_db = {}
dict_col = {}
children_id = database_total
database_id = 0
for database in databases:
    children = []
    cur_database = client[database]
    collections = cur_database.list_collection_names()
    # 删除.files和.chunks文件
    print("===================当前在的数据库是：" + str(database))
    for collection in collections:
        # print(collection)
        # 删除.chunks集合
        if ('.chunks') in collection:
            collections.remove(collection)
    # print(collections)

    for collection in collections:
        # print(collection)
        # 删.files集合
        if ('.files') in collection:
            collections.remove(collection)
    # print(collections)

    # 将数据按前端数据要求存放
    for collection in collections:
        children_id += 1
        dict_col = {
            'id': children_id,
            'label': collection,
            'isEdit': False,  # 主要用于前端判断添加、修改、删除按钮
            '_database': database,  # 属于哪个数据库，后续便于修改集合名称
        }
        children.append(dict_col)
    print(children)
    database_id += 1
    dict_db = {
        'id': database_id,
        'label': database,
        'isEdit': True,  # 主要用于前端判断添加、修改、删除按钮
        'children': children
    }
    list_db.append(dict_db)
print(list_db)
