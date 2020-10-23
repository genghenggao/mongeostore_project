'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-08-26 18:15:34
LastEditors: henggao
LastEditTime: 2020-10-23 15:08:06
'''
# from djongo import models

# from _datetime import datetime
# from django.contrib.auth.models import AbstractUser
# from django.db import models
# Create your models here.


# class News(models.Model):
#     title = models.CharField(verbose_name="采集点", max_length=50)
#     author = models.CharField(verbose_name="记录人员", max_length=10)
#     desc = models.CharField(verbose_name="简介", max_length=100)
#     content = models.TextField(verbose_name="描述")
#     create_time = models.DateTimeField(auto_now_add=True)
#     update_time = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = '测线'
#         verbose_name_plural = verbose_name


# class Mysegy(models.Model):
#     num_id = models.CharField(verbose_name="编号", max_length=50)
#     x_line = models.FloatField(default=0)
#     y_line = models.FloatField(default=0)
#     value = models.FloatField(default=0)
#     author = models.CharField(
#         verbose_name="记录人员", max_length=10, default="henggao")
#     create_time = models.DateTimeField(auto_now_add=True)
#     update_time = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.num_id


######## Mongeostore注册#########
# 用户
# 继承 Django 自带的User
# class UserInfo(AbstractUser):
#     ## AbstractUser自带一些字段 ##
#     # username = models.CharField(verbose_name='用户名', max_length=32)
#     # email = models.EmailField(verbose_name='邮箱', max_length=32)
#     # password = models.CharField(verbose_name='密码', max_length=32)
#     mobile = models.CharField(verbose_name='手机号', max_length=32, unique=True)
#     email_active = models.BooleanField(default=False, verbose_name='邮箱验证状态')

#     class Meta:
#         verbose_name = "用户"
#         verbose_name_plural = verbose_name

#     def __str__(self):
#         return self.username

# 短信验证码


# class VerifyCode(models.Model):
#     code = models.CharField(max_length=10, verbose_name="验证码")
#     mobile = models.CharField(max_length=11, verbose_name="电话号码")
#     # 这里不能加 ()， 如果加了的话，就会用编译的时间作为当前时间
#     add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

#     class Meta:
#         verbose_name = "短信验证码"
#         verbose_name_plural = verbose_name

#     def __str__(self):
#         return self.code


# 学生测试序列化
# class StudentsModel(models.Model):
#     email = models.EmailField()
#     content = models.CharField(max_length=200)
#     created = models.DateTimeField()
#     port = models.IntegerField()


from djongo import models
from _datetime import datetime
# mongeostore #


class UserInfo(models.Model):
    # 使用Djongo的Model、由于官方文档还没有类似Django中的AbstractUser
    username = models.CharField(verbose_name='用户名', max_length=32, unique=True)
    email = models.EmailField(
        verbose_name='邮箱', max_length=32, unique=True, null=True, blank=True)
    # 设置允许为空，因为前端登录只有一个值，是username，所以mobile可以为空
    mobile = models.CharField(
        verbose_name='手机号', max_length=32, unique=True, null=True, blank=True)
    password = models.CharField(verbose_name='密码', max_length=32)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class SmsCode(models.Model):
    """"验证码"""
    mobile = models.CharField(verbose_name='手机号', max_length=32)
    smscode = models.CharField(verbose_name='验证码', max_length=8)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "手机验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code


# class UploadFile(models.Model):
#     """上传文件"""
#     filename = models.CharField(verbose_name="文件名", max_length=56)
#     author = models.CharField(verbose_name="记录人员", max_length=56)
#     upload_time = models.DateTimeField(auto_now_add=True)
#     desc = models.CharField(verbose_name="简介", max_length=100)

#     class Meta:
#         verbose_name = "上传元数据"
#         verbose_name_plural = verbose_name

#     def __str__(self):
#         return self.filename

class UploadInfo(models.Model):
    '''
    上传文件
    '''
    name = models.CharField(max_length=255)
    upload_date = models.DateTimeField()
    path = models.CharField(max_length=255)
    md5 = models.CharField(max_length=33, default='')
    size = models.CharField(max_length=30, default=0)

    
    class Meta:
        verbose_name = "上传数据"
        verbose_name_plural = verbose_name

    def __str__(self): 
        return self.name