'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-12-16 21:38:16
LastEditors: henggao
LastEditTime: 2020-12-23 14:15:09
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

]
