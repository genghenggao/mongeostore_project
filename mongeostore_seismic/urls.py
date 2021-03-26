'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-12-16 21:38:16
LastEditors: henggao
LastEditTime: 2021-03-24 16:18:54
'''
from django.urls import include, path

from . import views
from .views import *
from rest_framework import routers
router = routers.DefaultRouter()
# router.register(r'drillmeta', DrillMetaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('seismicinfo/', SeismicInfoView.as_view(),
         name='seismicinfo'),  # 地震元数据查询上传
    path('editseismicinfo/', views.EditSeismicInfo,
         name="editseismicinfo"),  # 地震元数据编辑
    path('deleteseismicinfo/', views.DeleteSeismicInfo,
         name="deleteseismicinfo"),  # 地震元数据删除
    path('seismicinfosearch/', SeismicInfoSearch.as_view(),
         name="seismicinfosearch"),  # 地震元数据查询
    path('seismicfiledownload/', views.SeismicFileDownload,
         name="seismicfiledownload"),  # 地震元数据删除
    path('seismicfileread/', views.SeismicFileRead,
         name="seismicfileread"),  # 地震数据解析，获取文件
    path('seismicheaderquery/', views.SeismicHeaderQuery,
         name="seismicheaderquery"),  # 地震数据解析，获取文件
    path('seismicprofilequery/', views.SeismicProfileQuery,
         name="seismicprofilequery"),  # 地震数据解析，地震剖面查看
    path('Seismicanalysisdelete/', views.SeismicAnalysisDelete,
         name="Seismicanalysisdelete"),  # 地震数据解析，删除文件
    path('seismicanalysisupload/', SeismicAnalysisUpload.as_view(),
         name="seismicanalysisupload"),  # 地震数据解析，上传本地文件
    path('analysisclouddown/', views.AnalysisCloudDown,
         name="analysisclouddown"),  # 地震数据解析，下载数据库云端数据
    path('seismicprofilepic/', views.SeismicProfilePic,
         name="seismicprofilepic"),  # 地震数据解析，查看地震剖面图

# 遥感数据
    path('remoteinfo/', RemoteInfoView.as_view(),
         name='remoteinfo'),  # 遥感元数据查询上传
    path('editremoteinfo/', views.EditRemoteInfo,
         name="editremoteinfo"),  # 遥感元数据编辑
    path('deleteremoteinfo/', views.DeleteRemoteInfo,
         name="deleteremoteinfo"),  # 遥感元数据删除
    path('remoteinfosearch/', RemoteInfoSearch.as_view(),
         name="remoteinfosearch"),  # 遥感元数据查询
    path('remotefiledownload/', views.RemoteFileDownload,
         name="remotefiledownload"),  # 遥感元数据删除

# 测井数据
    path('logginginfo/', LoggingInfoView.as_view(),
         name='logginginfo'),  # 测井元数据查询上传
    path('editlogginginfo/', views.EditLoggingInfo,
         name="editlogginginfo"),  # 测井元数据编辑
    path('deletelogginginfo/', views.DeleteLoggingInfo,
         name="deletelogginginfo"),  # 测井元数据删除
    path('logginginfosearch/', LoggingInfoSearch.as_view(),
         name="logginginfosearch"),  # 测井元数据查询
    path('loggingfiledownload/', views.LoggingFileDownload,
         name="loggingfiledownload"),  # 测井元数据删除         

# 地质数据
    path('geologicalinfo/', GeologicalInfoView.as_view(),
         name='geologicalinfo'),  # 地质元数据查询上传
    path('editgeologicalinfo/', views.EditGeologicalInfo,
         name="editgeologicalinfo"),  # 地质元数据编辑
    path('deletegeologicalinfo/', views.DeleteGeologicalInfo,
         name="deletegeologicalinfo"),  # 地质元数据删除
    path('geologicalinfosearch/', GeologicalInfoSearch.as_view(),
         name="geologicalinfosearch"),  # 元数据查询
    path('geologicalfiledownload/', views.GeologicalFileDownload,
         name="geologicalfiledownload"),  # 元数据删除         
]
