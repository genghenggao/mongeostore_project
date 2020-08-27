'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-08-26 18:15:34
LastEditors: henggao
LastEditTime: 2020-08-27 20:40:23
'''
from djongo import models
# from django.db import models
# Create your models here.


class News(models.Model):
    title = models.CharField(verbose_name="采集点", max_length=50)
    author = models.CharField(verbose_name="记录人员", max_length=10)
    desc = models.CharField(verbose_name="简介", max_length=100)
    content = models.TextField(verbose_name="描述")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '测线'
        verbose_name_plural = verbose_name


class Mysegy(models.Model):
    num_id = models.CharField(verbose_name="编号", max_length=50)
    x_line = models.FloatField()
    y_line = models.FloatField()
    value = models.FloatField()
    author = models.CharField(verbose_name="记录人员", max_length=10)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.num_id
