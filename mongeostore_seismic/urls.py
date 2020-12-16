'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-12-16 21:38:16
LastEditors: henggao
LastEditTime: 2020-12-16 22:05:52
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
         name='seismicinfo'),  # 钻孔定位表数据查询
    # path('deletedrilllocation/', views.DeleteDrillLocation,
    #      name="deletedrilllocation"),  # 钻孔定位数据删除
]
