'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-11-04 11:16:50
LastEditors: henggao
LastEditTime: 2020-11-05 09:22:21
'''
from bson.json_util import dumps
import pymongo
import codecs
import csv

client = pymongo.MongoClient("192.168.55.110", 20000)
database = "segyfile"
db = client[database]
collection = "data"
db_coll = db[collection]


# 下载
# with codecs.open('./mongeostore_env/upload/data.csv', 'w', 'utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     # 这里我就给了2个字段名，如果你要输出更多的字段，继续后面添加
#     writer.writerow(['rid', 'vip'])
#     # 第一个{}实际上是筛选数据的若干条件，我这里没给条件，所以直接给的一个空的大括号
#     # 后面的字典则是mongo中的字段名，你想筛选的字段
#     for d in db_coll.find({}, {'rid': True, 'vip': True}):
#         writer.writerows([[d['rid'], d['vip']]])

# 查询
datainfo = []
for document in db_coll.find():

    # print(document)
    datainfo.append(document)
    print(type(datainfo))
    print(datainfo)
    dumps(datainfo)
    print("===========================")
    print(type(datainfo))
    print(datainfo)
