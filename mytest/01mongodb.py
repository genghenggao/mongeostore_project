'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-09-16 14:38:30
LastEditors: henggao
LastEditTime: 2020-09-17 16:29:50
'''
import datetime
import pymongo
from pymongo import MongoClient
from rest_framework.exceptions import ValidationError

client = MongoClient("192.168.55.110", 27017)
collection = client.mobilecode.expire
collection.create_index(
    [("time", pymongo.ASCENDING)], expireAfterSeconds=66)
data = {
    "mobile": 15351818127,
    "code": 123456,
}
# collection.insert(data)
dblist = client.list_database_names()
code = collection.find_one()
a = 15351818127
print(code)
# print(type(a))
mobilecode = collection.find_one({"mobile": str(a)})
# print(dblist)
# {'_id': ObjectId('5f6315202257bca6e0a7d470'), 'mobile': 15351818127, 'code': 123456}
print(mobilecode)
print(mobilecode['code'])  # 123456
print(type(mobilecode['code']))  # int
# print(type(mobilecode))
# print(collection)
if not mobilecode:

    print("success")
    raise ValidationError("验证码错误，请重新输入")

data1 = code['code']
data2 = code['mobile']
print(data1)
print(type(data1))  #<class 'int'>
print(data2)
print(type(data2))  #<class 'str'>