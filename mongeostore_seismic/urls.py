'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-12-16 21:38:16
LastEditors: henggao
LastEditTime: 2020-12-17 16:40:42
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
]