'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-08-26 18:15:34
LastEditors: henggao
LastEditTime: 2020-09-02 16:23:19
'''
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from .models import Mysegy
import random
from utils.tencent.sms import send_sms_single
from django.shortcuts import render, HttpResponse
from mongeostore_v1 import settings
# Create your views here.


@require_http_methods(['GET'])
def add_segy(request):
    response = {}
    try:
        segy = Mysegy(num_id=request.GET.get('num_id'))
        segy.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(['GET'])
def show_segys(request):
    response = {}
    try:
        segys = Mysegy.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", segys))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

# 发送短信验证


def send_sms(request):
    '''发送短信
        ?tpl=login  -> 611307
        ?tpl=register -> 611200

    '''
    tpl = request.GET.get('tpl')
    template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
    if not template_id:
        return HttpResponse('模板不存在')

    code = random.randrange(1000, 9999)
    res = send_sms_single('15351818127', template_id, [code, ])
    if res['result'] == 0:
        return HttpResponse('成功')
    else:
        return HttpResponse(res['errmsg'])


#####   mongeostore  ######
from django import forms
from mongeostore_app import models

class RegisterForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = '__all__'
        
def register(request):
    form = RegisterForm()
    return render(request,'register.html',{'form':form})