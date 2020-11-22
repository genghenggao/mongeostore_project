'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-23 21:47:34
LastEditors: henggao
LastEditTime: 2020-11-22 19:08:12
'''
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

    ZK_num = models.CharField(max_length=20)
    Depth = models.FloatField(max_length=20)
    Azimuth = models.FloatField(max_length=30)
    Inclination = models.FloatField(max_length=30)

    class Meta:
        verbose_name = "钻孔数据"
        verbose_name_plural = verbose_name
        app_label = 'drill'  # 如果指定将在drill对应的数据库下创建数据表
        db_table = '钻孔数据测斜表'  # 自定义表名称

    def __str__(self):
        """
        docstring
        """
        return self.ZK_num
