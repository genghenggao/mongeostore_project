'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2021-01-20 16:13:18
LastEditors: henggao
LastEditTime: 2021-01-21 10:39:06
'''
from mongoengine import connect
from mongoengine.context_managers import switch_collection
from mongoengine.document import Document
from mongoengine.fields import IntField, StringField

import settings
from mongoengine import *
# connect('钻孔数据管理子系统', host='192.168.55.110', port=20000)

# url = "mongodb+srv://henggao:tel123456@mongeostore.tgjjd.mongodb.net/用户信息管理子系统?retryWrites=true&w=majority"
# connect(host=url, port=20000)

# url = "mongodb+srv://henggao:tel123456@mongeostore.tgjjd.mongodb.net"
# connect(db='用户信息管理子系统', host=url, port=20000)
connect(db='用户信息管理子系统', host=settings.MONGODB_Atlas_URL, port=20000)

class Users(Document):
    name = StringField(required=True, max_length=200)
    age = IntField(required=True)

# user1 = Users(
#     name='zz',
#     age=112
# )

# user1.save()
# print(user1.name)
# user1.name = 'zz11'
# user1.save()
# print(user1.name)

with switch_collection(Users, '用户') as user:
    user(name='henggao',age=28).save()  # 将数据保存至 用户 集合


    