'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-12-16 21:38:35
LastEditors: henggao
LastEditTime: 2020-12-16 21:38:35
'''
from .models import SeismicInfo
from rest_framework_mongoengine.serializers import DocumentSerializer
class SeismicInfoSerializer(DocumentSerializer):
    '''钻孔数据管理子系统定位表数据'''
    class Meta:
        model = SeismicInfo
        fields = "__all__"