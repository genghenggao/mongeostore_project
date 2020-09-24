from django.shortcuts import render

# Create your views here.
'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-09-24 15:33:42
LastEditors: henggao
LastEditTime: 2020-09-24 19:48:52
'''
from verification.serializer import SmsSerializer
from random import choice
from utils.tencent.sms import send_sms_single
from mongeostore_v1 import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from pymongo.mongo_client import MongoClient
import pymongo
from rest_framework import viewsets, mixins


class SmsCodeViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """
    发送短信验证码
    """
    serializer_class = SmsSerializer

    def generate_code(self):
        """
        生成四位数验证码
        :return:
        """
        seeds = '1234567890'
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 自定义的create()的内容
        # 从validated_data中获取mobile
        mobile = serializer.validated_data['mobile']
        # 随机生成code
        code = self.generate_code()

        # 发送验证码短信
        # yun_pian = YunPian(APIKEY)
        # sms_status = yun_pian.send_sms(code=code, mobile=mobile)
        tpl = self.request.GET.get('tpl')
        print(tpl)
        template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
        if not template_id:
            raise ValidationError("短信模板错误")

        # 发送短信
        sms = send_sms_single(mobile, template_id, [code, ])
        # if sms["result"] != 0:
        #     raise ValidationError("短信发送失败，{}".format['errmsg'])
        if sms['code'] != 0:
            return Response({
                'mobile': sms['code']
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            # code_record = VerifyCode(code=code, mobile=mobile)
            # # 保存验证码
            # code_record.save()
            client = MongoClient("192.168.55.110", 27017)
            collection = client.mobilecode.expire
            collection.create_index(
                [("time", pymongo.ASCENDING)], expireAfterSeconds=66)
            data = {
                "mobile": mobile,  # 注意这个存入的类型，这样传入的是字符串str
                "code": code,
            }
            collection.insert(data)
        return Response({
            'mobile': mobile
        }, status=status.HTTP_201_CREATED)
