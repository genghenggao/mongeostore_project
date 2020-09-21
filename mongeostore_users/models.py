'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-09-19 06:54:56
LastEditors: henggao
LastEditTime: 2020-09-19 07:22:33
'''
# from django.db import models 
# #使用djongo
from djongo import models
# Create your models here.


class UserInfo(models.Model):
        # 使用Djongo的Model、由于官方文档还没有类似Django中的AbstractUser
    username = models.CharField(verbose_name='用户名', max_length=32, unique=True)
    email = models.EmailField(verbose_name='邮箱', max_length=32, unique=True)
    mobile = models.CharField(verbose_name='手机号', max_length=32, unique=True)
    password = models.CharField(verbose_name='密码', max_length=32)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
