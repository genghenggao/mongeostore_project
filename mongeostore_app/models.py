'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-08-26 18:15:34
LastEditors: henggao
LastEditTime: 2020-09-02 16:12:08
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
    x_line = models.FloatField(default=0)
    y_line = models.FloatField(default=0)
    value = models.FloatField(default=0)
    author = models.CharField(verbose_name="记录人员", max_length=10,default="henggao")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.num_id


######## Mongeostore注册#########
class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32)
    email = models.EmailField(verbose_name='邮箱', max_length=32)
    mobile_phone = models.CharField(verbose_name='手机号', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=32)

    