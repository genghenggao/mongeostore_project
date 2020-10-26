'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-24 09:45:03
LastEditors: henggao
LastEditTime: 2020-10-26 22:18:23
'''
from rest_framework import serializers
from .models import FileInfo, FileInfo2


class FileInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileInfo
        files = "__all__"


class FileInfo2Serializer(serializers.ModelSerializer):
    class Meta:
        model = FileInfo2
        files = "__all__"
