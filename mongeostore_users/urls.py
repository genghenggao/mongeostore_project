'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-09-19 07:16:33
LastEditors: henggao
LastEditTime: 2020-09-24 15:03:47
'''
from django.urls import path, re_path
from django.conf.urls import url, include
from .views import UserInfoView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    # path('api/', include(mongeostore_app.urls)),
    path('user/', UserInfoView.as_view(), name='uesrinfo'),
    # path('', TemplateView.as_view(template_name="index.html")),
    # re_path(r'.*', TemplateView.as_view(template_name='index.html')),
    path('login',obtain_jwt_token),   #jwt自带的功能
]
