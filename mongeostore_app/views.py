'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-08-26 18:15:34
LastEditors: henggao
LastEditTime: 2020-08-27 21:10:49
'''
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from .models import Mysegy
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
        segys = Mysegy.object.filter()
        response['list'] = json.loads(serializers.serialize("json", segys))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)