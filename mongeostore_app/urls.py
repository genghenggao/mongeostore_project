'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-08-27 21:02:36
LastEditors: henggao
LastEditTime: 2020-10-14 21:56:12
'''
# # 这是新建的urls，用于将接口添加到路由里
# from django.conf.urls import url, include
# from django.urls import path, include

# from rest_framework.routers import DefaultRouter
# # from . import views
# from mongeostore_app import views

# router = DefaultRouter()
# router.register('mongeostore_app', views.RegisterView, basename='register')

# urlpatterns = [
#     # 主页MySegy
#     # url(r"add_segy$", views.add_segy),
#     # url(r"show_segys$", views.show_segys),

#     # students测试序列化
#     url(r"students/", views.StudentsView.as_view(),name="students"),


#     # 注册
#     url(r'^register/$', views.RegisterView.as_view(), name='register'),
#     url(r'^usernames/(?P<username>[a-zA-Z0-9_-]{5,20})/count/$',
#         views.UsernameCountView.as_view(), ),
#     url(r'^mobiles/(?P<mobile>1[3-9]\d{9})/count/$',
#         views.MobileCountView.as_view(), ),
#     url(r'^login/$', views.LoginView.as_view()),

#     ####    mongeostore ###########
# basic URL Configurations
from django.urls import include, path
# import routers
from rest_framework import routers

# import everything from views
from .views import *
# 添加RegisterView视图
from .views import RegisterView, CheckUsername, CheckEmail, CheckMobile, LoginViewTest
from . import views
from rest_framework.compat import re_path
from django.views.generic import TemplateView
# jwt内部实现的登陆视图
from rest_framework_jwt.views import obtain_jwt_token

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'userinfo', UserInfoViewSet)

# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    # path('send_sms/', views.send_sms)
    path('send_sms/', MobileCountView.as_view(), name='send_sms'),
    path('username/', CheckUsername.as_view(), name='username'),
    path('email/', CheckEmail.as_view(), name='email'),
    path('mobile/', CheckMobile.as_view(), name='mobile'),
    # path('smscode/', CheckSmscode.as_view(), name='smscode'),
    path('register/', RegisterView.as_view(), name='register'),
    path('userlogin/', LoginViewTest.as_view(), name='login'),
    path(r"login", obtain_jwt_token),

    path('', TemplateView.as_view(template_name="index.html")),

    re_path(r'.*', TemplateView.as_view(template_name='index.html')),
    path('uploadfile/',views.upload_file)
]
