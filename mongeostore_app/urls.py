'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-08-27 21:02:36
LastEditors: henggao
LastEditTime: 2020-08-27 21:11:04
'''
#这是新建的urls，用于将接口添加到路由里
from django.conf.urls import url,include 
from . import views

urlpatterns = [
    # 主页
    url(r"add_segy$", views.add_segy),
    url(r"show_segys$", views.show_segys),
]