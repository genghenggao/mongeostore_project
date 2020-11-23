'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-23 21:53:21
LastEditors: henggao
LastEditTime: 2020-11-23 22:36:11
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
    path('showcommondata/', views.ShowCommonData,
         name="showcommondata"),  # Collection展示数据
    path('commoneditdata/', views.CommonEditData,
         name="commoneditdata"),  # Collection编辑数据
    path('commondeletedata/', views.CommonDeleteData,
         name="commondeletedata"),  # Collection删除表格数据
    path('commonadd_data/', views.CommonAddData,
         name="commonadd_data"),  # Collection添加数据
    path('commonquerydata/', views.CommonQueryData,
         name="commonquerydata"),  # Collection数据搜索

    path('showdrillclination/', DrillInclinationPageView.as_view(),
         name="showdrillclination"),  # 钻孔测斜表
    path('commonuploadexcel/', CommonUploadExcel.as_view(),
         name="commonuploadexcel"),  # 上传Excel
    path('commonuploadcsv/', CommonUploadCSV.as_view(),
         name="commonuploadcsv"),  # 上传CSV
    path('commonuploadmeta/', CommonUploadMeta.as_view(),
         name="commonuploadmeta"),  # 上传元数据到GridFS
    path('commonmetashow/', views.CommonMetaShow,
         name="commonmetashow"),  # GridFS 源数据表格展示，有点小问题
    path('commonfiledownload/', views.CommonFileDownload,
         name="commonfiledownload"),  # 下载元数据，还没完成


]
