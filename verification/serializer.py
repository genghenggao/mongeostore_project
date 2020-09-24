'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-09-24 15:42:23
LastEditors: henggao
LastEditTime: 2020-09-24 19:49:18
'''

import re
from rest_framework import serializers
from django.conf import settings

from django.contrib.auth import get_user_model
from django import http
import datetime
from _datetime import timedelta

# 通过这种方式获取定义的用户模型(不管是定义什么类名都是这样获取)
User = get_user_model()


class SmsSerializer(serializers.Serializer):
    """
    用于用户发送手机验证码的serializer类
    """
    mobile = serializers.CharField(label='手机号码', max_length=11, min_length=11, required=True,
                                   error_messages={'required': '手机号码必填', 'min_length': '手机号码格式错误',
                                                   'max_length': '手机号码格式错误'})

    def validate_mobile(self, mobile):
        """
        验证手机号码的函数
        :param mobile:
        :return:
        """

        # 判断用户是否已经注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError('该用户已经存在')

        # 正则判断手机号码格式
        if not re.match(settings.REGEX_MOBILE, mobile):
            raise serializers.ValidationError('手机号码格式错误')
        # 判断手机号是否合法
        # if not re.match(r'^1[3-9]\d{9}$', mobile):
        #     return http.HttpResponseForbidden('请输入正确的手机号码')

        # 验证码发送频率
        one_minute_age = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if User.objects.filter(add_time__gt=one_minute_age, mobile=mobile).count():
            raise serializers.ValidationError('请一分钟后再次发送')

        return mobile
