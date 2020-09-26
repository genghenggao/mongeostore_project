'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-09-19 07:16:43
LastEditors: henggao
LastEditTime: 2020-09-26 17:25:32
'''
from rest_framework import serializers
from .models import UserInfo
## mongeostore序列化 ## 
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo     #对应的Model中的类
        # fields = ("username", "mobile", "email",)
        fields = "__all__"  #字段，如果是__all__,就是表示列出所有的字段
        