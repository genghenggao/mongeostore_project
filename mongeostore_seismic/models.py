'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-12-16 21:36:57
LastEditors: henggao
LastEditTime: 2021-03-24 16:19:48
'''
from datetime import datetime
from django.db import models
from mongoengine import connect
from mongoengine.document import Document
from mongoengine.fields import DateTimeField, FileField, ImageField, StringField

# Create your models here.
# 设置数据库
connect(alias='default', db='地震数据管理子系统',
        host='192.168.55.110', port=20000)
connect(alias='seismic_system', db='地震数据管理子系统',
        host='192.168.55.110', port=20000)
connect(alias='remote_system', db='遥感数据管理子系统',
        host='192.168.55.110', port=20000)
connect(alias='logging_system', db='测井数据管理子系统',
        host='192.168.55.110', port=20000)
connect(alias='geological_system', db='地质数据管理子系统',
        host='192.168.55.110', port=20000)

class SeismicInfo(Document):
    '''地震数据上传'''
    seismic_filename = StringField(required=True)
    location = StringField(required=True)
    company_name = StringField(required=True)
    uploader = StringField(required=True)
    seismic_upload_date = DateTimeField(default=datetime.now(), required=True)
    project_name = StringField(required=True)
    filedata = FileField()
#     seismicprofile = ImageField(collection_name='seismicprofile')
#     filedata = FileField(collection_name='test')  # 设置Gridfs中的存储桶名称

    meta = {'db_alias': 'seismic_system',
            # 'collection': '地震数据Demo1', 'indexes': ['filename']}
            'collection': '地震数据', 'indexes': [{'fields': ['$seismic_filename', "$location"],
                                               'default_language': 'english',
                                               'weights': {'title': 10, 'content': 2}
                                               }]}

    def __str__(self) -> str:
        """
        docstring
        """
        return self.seismic_filename


class RemoteInfo(Document):
    '''遥感数据上传'''
    remote_filename = StringField(required=True)
    location = StringField(required=True)
    company_name = StringField(required=True)
    uploader = StringField(required=True)
    remote_upload_date = DateTimeField(default=datetime.now(), required=True)
    project_name = StringField(required=True)
    filedata = FileField(db_alias='remote_system', collection_name='fs')
#     seismicprofile = ImageField(collection_name='seismicprofile')
#     filedata = FileField(collection_name='test')  # 设置Gridfs中的存储桶名称

    meta = {'db_alias': 'remote_system',
            # 'collection': '地震数据Demo1', 'indexes': ['filename']}
            'collection': '遥感影像', 'indexes': [{'fields': ['$remote_filename', "$location"],
                                               'default_language': 'english',
                                               'weights': {'title': 10, 'content': 2}
                                               }]}

    def __str__(self) -> str:
        """
        docstring
        """
        return self.remote_filename


class LoggingInfo(Document):
    '''测井数据上传'''
    logging_filename = StringField(required=True)
    location = StringField(required=True)
    company_name = StringField(required=True)
    uploader = StringField(required=True)
    logging_upload_date = DateTimeField(default=datetime.now(), required=True)
    project_name = StringField(required=True)
    filedata = FileField(db_alias='logging_system', collection_name='fs')
#     seismicprofile = ImageField(collection_name='seismicprofile')
#     filedata = FileField(collection_name='test')  # 设置Gridfs中的存储桶名称

    meta = {'db_alias': 'logging_system',
            # 'collection': '地震数据Demo1', 'indexes': ['filename']}
            'collection': '测井数据', 'indexes': [{'fields': ['$logging_filename', "$location"],
                                               'default_language': 'english',
                                               'weights': {'title': 10, 'content': 2}
                                               }]}

    def __str__(self) -> str:
        """
        docstring
        """
        return self.logging_filename


class GeologicalInfo(Document):
    '''地质数据上传'''
    geological_filename = StringField(required=True)
    location = StringField(required=True)
    company_name = StringField(required=True)
    uploader = StringField(required=True)
    geological_upload_date = DateTimeField(default=datetime.now(), required=True)
    project_name = StringField(required=True)
    filedata = FileField(db_alias='geological_system', collection_name='fs')
#     seismicprofile = ImageField(collection_name='seismicprofile')
#     filedata = FileField(collection_name='test')  # 设置Gridfs中的存储桶名称

    meta = {'db_alias': 'geological_system',
            # 'collection': '地震数据Demo1', 'indexes': ['filename']}
            'collection': '地质数据', 'indexes': [{'fields': ['$geological_filename', "$location"],
                                               'default_language': 'english',
                                               'weights': {'title': 10, 'content': 2}
                                               }]}

    def __str__(self) -> str:
        """
        docstring
        """
        return self.geological_filename
