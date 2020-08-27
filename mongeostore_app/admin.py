'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-08-26 18:15:34
LastEditors: henggao
LastEditTime: 2020-08-27 14:32:04
'''
from django.contrib import admin

# Register your models here.
from mongeostore_app.models import News
admin.site.register(News)