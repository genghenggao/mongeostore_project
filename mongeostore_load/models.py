'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-23 21:47:34
LastEditors: henggao
LastEditTime: 2020-11-04 22:13:12
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
