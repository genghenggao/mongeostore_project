'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-23 21:53:21
LastEditors: henggao
LastEditTime: 2020-11-09 21:30:47
'''
from .views import FileInfoView
from django.urls import include, path

from . import views
from .views import *

urlpatterns = [
    path('uploadfile/', views.uploadfile, name="uploadefile"),
    path('fileinfo/', FileInfoView.as_view(), name="fileinfo"),
    path('fileshow/', views.FileShow, name="fileshow"),
    path('filedownload/', views.filedownload, name="filedownload"),
    path('showdata/', views.ShowData, name="showdata"),
    path('uploadcsv/', UploadCSV.as_view(), name="uploadcsv"),
    path('uploadexcel/', UploadExcel.as_view(), name="uploadexcel"),
    path('editdata/', views.EditData, name="editdata"),
    path('deletedata/', views.DeleteData, name="deletedata"),
]
