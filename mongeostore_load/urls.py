'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-23 21:53:21
LastEditors: henggao
LastEditTime: 2020-11-22 22:43:44
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
    path('add_data/', views.AddData, name="add_data"),
    path('querydata/', views.QueryData, name="add_data"),
    path('showdatabase/', views.ShowDataBase, name="showdatabase"),
    path('adddatabase/', views.AddDataBase, name="adddatabase"),
    path('deletedatabase/', views.DeleteDataBase, name="deletedatabase"),
    path('addcollection/', views.AddCollection, name="addcollection"),
    path('deletecollection/', views.DeleteCollection, name="deletecollection"),
    path('editdatabasename/', views.EditDataBase, name="editdatabasename"),
    # mongeostore
    path('showcommondata/', views.ShowCommonData, name="showcommondata"),
    path('showdrillclination/', DrillInclinationPageView.as_view(),
         name="showdrillclination"),  # 钻孔测斜表
    path('commonuploadexcel/', CommonUploadExcel.as_view(),
         name="commonuploadexcel"),  # 上传Excel
    path('commonuploadcsv/', CommonUploadCSV.as_view(),
         name="commonuploadcsv"),  # 上传CSV
    path('commonuploadmeta/', CommonUploadMeta.as_view(),
         name="commonuploadmeta"),  # 上传元数据到GridFS


]
