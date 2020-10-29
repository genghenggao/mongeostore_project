'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-24 09:45:03
LastEditors: henggao
LastEditTime: 2020-10-29 09:46:32
'''
from rest_framework import serializers
from .models import FileInfo


class FileInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileInfo
        files = "__all__"
