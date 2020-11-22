'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-24 09:45:03
LastEditors: henggao
LastEditTime: 2020-11-22 19:04:32
'''
from django.db.models import fields
from rest_framework import serializers
from .models import DrillInclinationModel, FileInfo


class FileInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileInfo
        files = "__all__"


class DrillInclinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrillInclinationModel
        fields = "__all__"
