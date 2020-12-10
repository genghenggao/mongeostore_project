'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-23 21:47:34
LastEditors: henggao
LastEditTime: 2020-12-10 22:38:04
'''
# from djongo.models.indexes import TwoDSphereIndex  //模块付费
from mongoengine import connect
from mongoengine.context_managers import switch_collection, switch_db
from mongoengine import *
from mongoengine.fields import FloatField, IntField, ListField, StringField
from mongoengine.document import Document
from djongo.storage import GridFSStorage
from django.conf import settings
from djongo import models

# Create your models here.


class FileInfo(models.Model):

    # _id = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    # type = models.CharField(max_length=255)
    size = models.CharField(max_length=30, default=0)
    upload_date = models.DateTimeField()
    publisher = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    md5 = models.CharField(max_length=33, default='')

    class Meta:
        verbose_name = "文件信息"
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.filename


class DrillInclinationModel(models.Model):
    '''
    DrillInclinationData
    '''
    # 要指定自定义主键，只需在其中一个字段上指定primary_key = True即可。如果Django看到你有明确设置Field.primary_key，它将不会添加自动ID列。
    _id = models.CharField(primary_key=True, max_length=50)  # 需要设置自定义主键
    ZK_num = models.CharField(max_length=20)
    Depth = models.FloatField(max_length=20)
    Azimuth = models.FloatField(max_length=30)
    Inclination = models.FloatField(max_length=30)

    class Meta:
        verbose_name = "测斜表"  # 易于理解和表述的对象名称，单数形式:
        verbose_name_plural = verbose_name  # 对象的复数表述名
        app_label = 'drill'  # 如果指定将在drill对应的数据库下创建数据表
        db_table = '测斜表'  # 自定义表名称，即是对应的Collection

    def __str__(self):
        """
        docstring
        """
        return self.ZK_num


# grid_fs_storage = GridFSStorage(
#     collection='钻孔元数据GridFS')  # 这里的base_url设置无效
# grid_fs_storage = GridFSStorage(
#     collection='钻孔元数据', base_url=''.join(['', '钻孔元数据/']))
# Define your GrifFSStorage instance
grid_fs_storage = GridFSStorage(location='', collection='钻孔信息元数据', base_url=''.join(
    ['', '']), database='drill')


class DrillMetaModel(models.Model):
    '''钻孔数据管理子系统元数据'''
    _id = models.CharField(max_length=255)
    zk_num = models.CharField(max_length=255)
    # type = models.CharField(max_length=255)
    zk_type = models.CharField(max_length=30)
    final_depth = models.CharField(max_length=255)
    # final_date = models.DateTimeField()
    # upload_date = models.DateTimeField()
    final_date = models.DateField()
    upload_date = models.DateField()
    project_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    uploader = models.CharField(max_length=255)
    # zk_histogram = models.ImageField(upload_to='InclinationMetaModels')
    zk_histogram = models.ImageField(
        upload_to='InclinationMetaModels', storage=grid_fs_storage)

    class Meta:
        verbose_name = "钻孔元数据名"
        verbose_name_plural = verbose_name
        # app_label = 'mongeostore_load'  # 如果指定将在drill对应的数据库下创建数据表
        db_table = '钻孔信息'  # 自定义表名称，即是对应的Collection，如何对应GriDFS

    def __str__(self) -> str:
        return self.zk_num


class DrillCoordniteModel(models.Model):
    """
    docstring
    """
    coordinate_E = models.FloatField(max_length=50)
    coordinate_N = models.FloatField(max_length=50)
    coordinate_R = models.FloatField(max_length=50)

    class Meta:
        abstract = True


class DrillLocationModel(models.Model):
    '''钻孔定位表'''
    _id = models.CharField(max_length=100)
    zk_num = models.CharField(max_length=50)
    coordinate_E = models.FloatField(max_length=50)
    coordinate_N = models.FloatField(max_length=50)
    coordinate_R = models.FloatField(max_length=50)
    # coordniate = models.ArrayField(model_container=DrillCoordniteModel)

    class Meta:
        verbose_name = "钻孔定位表"
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        """
        docstring
        """
        return self.zk_num


# 设置数据库
connect(alias='drill_system', db='钻孔数据管理子系统',
        host='192.168.55.110', port=20000)
connect(alias='rs_system', db='遥感数据管理子系统', host='192.168.55.110', port=20000)


class DrillLocation(Document):
    '''钻孔定位表'''
    name = StringField(required=True)
    locaton = ListField(required=True)
    # zk_num = StringField(required=True, max_length=200)
    # coordinate_E = FloatField(required=True, max_length=50)
    # coordinate_N = FloatField(required=True, max_length=50)
    # coordinate_R = FloatField(required=True, max_length=50)
    # coordniate = ListField()
    meta = {'db_alias': 'drill_system'}
