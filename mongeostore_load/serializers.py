'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-24 09:45:03
LastEditors: henggao
LastEditTime: 2020-12-10 22:24:18
'''
from django.db.models import fields
from rest_framework import serializers
from .models import DrillInclinationModel, DrillLocation, FileInfo, DrillMetaModel


class FileInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileInfo
        files = "__all__"


class DrillInclinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrillInclinationModel
        fields = "__all__"


class DrillMetaSerializer(serializers.ModelSerializer):
    '''钻孔数据管理子系统元数据'''
    class Meta:
        model = DrillMetaModel
        fields = "__all__"


# class DrillLoactionSerializer(serializers.ModelSerializer):
#     '''钻孔数据管理子系统定位表数据'''
#     class Meta:
#         model = DrillLocationModel
#         fields = "__all__"
from rest_framework_mongoengine.serializers import DocumentSerializer
class DrillLocationSerializer(DocumentSerializer):
    '''钻孔数据管理子系统定位表数据'''
    class Meta:
        model = DrillLocation
        fields = "__all__"
