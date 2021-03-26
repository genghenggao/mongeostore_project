'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-12-16 21:38:35
LastEditors: henggao
LastEditTime: 2021-03-24 16:03:22
'''
from .models import SeismicInfo
from .models import RemoteInfo
from .models import LoggingInfo, GeologicalInfo
from rest_framework_mongoengine.serializers import DocumentSerializer
class SeismicInfoSerializer(DocumentSerializer):
    '''地震数据管理子系统定位表数据'''
    class Meta:
        model = SeismicInfo
        fields = "__all__"
class RemoteInfoSerializer(DocumentSerializer):
    '''遥感数据管理子系统定位表数据'''
    class Meta:
        model = RemoteInfo
        fields = "__all__"


class LoggingInfoSerializer(DocumentSerializer):
    '''测井数据管理子系统定位表数据'''
    class Meta:
        model = LoggingInfo
        fields = "__all__"
class GeologicalInfoSerializer(DocumentSerializer):
    '''测井数据管理子系统定位表数据'''
    class Meta:
        model = GeologicalInfo
        fields = "__all__"