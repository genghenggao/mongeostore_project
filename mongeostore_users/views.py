'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-09-19 06:54:56
LastEditors: henggao
LastEditTime: 2020-09-26 17:25:48
'''
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class UserInfoView(APIView):

    def get(self,request,*args,**kwargs):
        return Response("...")
