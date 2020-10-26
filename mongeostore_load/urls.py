'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-23 21:53:21
LastEditors: henggao
LastEditTime: 2020-10-26 22:54:57
'''
from .views import FileInfo2View, FileInfoView
from django.urls import include, path

from . import views

urlpatterns = [
    path('uploadfile/', views.uploadfile, name="uploadefile"),
    path('fileinfo/', FileInfoView.as_view(), name="fileinfo"),
    path('fileinfo2/', FileInfo2View.as_view(), name="fileinfo2")
]
