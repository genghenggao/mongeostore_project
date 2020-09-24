'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-09-24 19:47:24
LastEditors: henggao
LastEditTime: 2020-09-24 20:10:55
'''

from django.urls import include, path
# 添加视图
# from .views import SmsCodeViewSet
from . import views
# specify URL Path for rest_framework
urlpatterns = [
    # path('send_sms/', views.SmsCodeViewSet.as_view(), name='send_sms'),
]
