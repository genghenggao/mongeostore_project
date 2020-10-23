'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-23 21:53:21
LastEditors: henggao
LastEditTime: 2020-10-23 22:07:40
'''
from django.urls import include, path

from . import views

urlpatterns= [
    path('uploadfile/', views.uploadfile,name="uploadefile"),
]