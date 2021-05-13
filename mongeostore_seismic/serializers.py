'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-12-16 21:38:35
LastEditors: henggao
LastEditTime: 2021-03-29 21:17:52
'''
from .models import SeiInterpretationInfo, SeihistoricalInfo, SeiprocessInfo, SeismicInfo
from .models import RemoteInfo
from .models import LoggingInfo, GeologicalInfo, HydrologicalInfo,SeiAcquisitionInfo
from rest_framework_mongoengine.serializers import DocumentSerializer
class SeismicInfoSerializer(DocumentSerializer):
    '''地震数据管理子系统地震数据'''
    class Meta:
        model = SeismicInfo
        fields = "__all__"

class SeiAcquisitionInfoSerializer(DocumentSerializer):
    '''地震数据管理子系统地震采集数据'''
    class Meta:
        model = SeiAcquisitionInfo
        fields = "__all__"
class SeiprocessInfoSerializer(DocumentSerializer):
    '''地震数据管理子系统地震处理数据'''
    class Meta:
        model = SeiprocessInfo
        fields = "__all__"
class SeiInterpretationInfoSerializer(DocumentSerializer):
    '''地震数据管理子系统地震解释数据'''
    class Meta:
        model = SeiInterpretationInfo
        fields = "__all__"
class SeihistoricalInfoSerializer(DocumentSerializer):
    '''地震数据管理子系统地震历史数据'''
    class Meta:
        model = SeihistoricalInfo
        fields = "__all__"

class RemoteInfoSerializer(DocumentSerializer):
    '''遥感数据管理子系统遥感数据'''
    class Meta:
        model = RemoteInfo
        fields = "__all__"


class LoggingInfoSerializer(DocumentSerializer):
    '''测井数据管理子系统测井数据'''
    class Meta:
        model = LoggingInfo
        fields = "__all__"
class GeologicalInfoSerializer(DocumentSerializer):
    '''地质数据管理子系统地质数据'''
    class Meta:
        model = GeologicalInfo
        fields = "__all__"
class HydrologicalInfoSerializer(DocumentSerializer):
    '''水文数据管理子系统水文数据'''
    class Meta:
        model = HydrologicalInfo
        fields = "__all__"