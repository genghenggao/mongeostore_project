'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-23 21:47:34
LastEditors: henggao
LastEditTime: 2020-10-26 22:15:32
'''
from djongo import models

# Create your models here.


class FileInfo(models.Model):
    filename = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    upload_date = models.DateTimeField()
    path = models.CharField(max_length=255)
    md5 = models.CharField(max_length=33, default='')
    size = models.CharField(max_length=30, default=0)

    class Meta:
        verbose_name = "文件信息"
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.filename


class FileInfo2(models.Model):

    name = models.CharField(max_length=255)
    upload_date = models.DateTimeField()
    path = models.CharField(max_length=255)
    md5 = models.CharField(max_length=33, default='')
    size = models.CharField(max_length=30, default=0)
    class Meta:
        verbose_name = "文件信息"
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.name
