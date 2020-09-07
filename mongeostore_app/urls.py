'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-08-27 21:02:36
LastEditors: henggao
LastEditTime: 2020-09-03 14:56:39
'''
# 这是新建的urls，用于将接口添加到路由里
from django.conf.urls import url, include
from django.urls import path, include

from rest_framework.routers import DefaultRouter
# from . import views
from mongeostore_app import views

router = DefaultRouter()
router.register('mongeostore_app', views.RegisterView, basename='register')

urlpatterns = [
    # 主页MySegy
    # url(r"add_segy$", views.add_segy),
    # url(r"show_segys$", views.show_segys),

    # students测试序列化
    url(r"students/", views.StudentsView.as_view(),name="students"),


    # 注册
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^usernames/(?P<username>[a-zA-Z0-9_-]{5,20})/count/$',
        views.UsernameCountView.as_view(), ),
    url(r'^mobiles/(?P<mobile>1[3-9]\d{9})/count/$',
        views.MobileCountView.as_view(), ),
    url(r'^login/$', views.LoginView.as_view()),

    ####    mongeostore ###########
]
