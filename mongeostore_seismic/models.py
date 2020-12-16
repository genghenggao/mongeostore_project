'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-12-16 21:36:57
LastEditors: henggao
LastEditTime: 2020-12-16 23:04:04
'''
from datetime import datetime
from django.db import models
from mongoengine import connect
from mongoengine.document import Document
from mongoengine.fields import DateTimeField, FileField, StringField

# Create your models here.
# 设置数据库
connect(alias='drill_system', db='钻孔数据管理子系统',
        host='192.168.55.110', port=20000)
connect(alias='rs_system', db='遥感数据管理子系统', host='192.168.55.110', port=20000)
connect(alias='geo_example', db='geo_example',
        host='192.168.55.110', port=20000)


class SeismicInfo(Document):
    '''钻孔定位表'''
    filename = StringField(required=True)
    location = StringField(required=True)
    company_name = StringField(required=True)
    uploader = StringField(required=True)
    upload_date = DateTimeField(default=datetime.now(), required=True)
    project_name = StringField(required=True)
    filedata = FileField()

    meta = {'db_alias': 'drill_system',
            'collection': '地震数据Demo1', 'indexes': ['filename']}

    def __str__(self) -> str:
        """
        docstring
        """
        return self.filename
