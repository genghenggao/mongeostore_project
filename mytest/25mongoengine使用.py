'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-12-10 19:17:01
LastEditors: henggao
LastEditTime: 2020-12-10 21:25:43
'''
# import datetime
from mongoengine import connect
from mongoengine.document import Document
from mongoengine.fields import IntField, StringField
from mongoengine import *
from mongoengine.context_managers import switch_collection, switch_db

connect(alias='drill_system', db='钻孔数据管理子系统',
        host='192.168.55.110', port=20000)
connect(alias='rs_system', db='遥感数据管理子系统', host='192.168.55.110', port=20000)


class Users(Document):
    name = StringField(required=True, max_length=200)
    age = IntField(required=True)
    meta = {'db_alias': 'rs_system'}


with switch_collection(Users, 'group2000') as Users:
    # Users(name='hello Group 2000 collection!').save()  # 将数据保存至 group2000 集合
    # Users(name='Ross').save()  # ===》 这时会将数据保存至 'archive-user-db'

    user1 = Users(
        name='zz',
        age=112
    )
    user1.save()
    print(user1.name)
    user1.name = 'zz11'
    user1.save()
    print(user1.name)
