'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-08-26 18:15:34
LastEditors: henggao
LastEditTime: 2020-09-03 17:00:19
'''
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from .models import Mysegy
import random
from utils.tencent.sms import send_sms_single
from mongeostore_v1 import settings
import re
from django.contrib.auth import authenticate, login
from django.db import DatabaseError
from django.shortcuts import HttpResponse, redirect, render
from django import http
from django.urls import reverse
from django.views import View
from mongeostore_app.models import UserInfo
from utils.response_code import RETCODE
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


#####   mongeostore 注册 ######
class RegisterView(View):
    """用户注册"""

    def get(self, request):
        """
        提供注册界面
        :param request: 请求对象
        :return: 注册界面
        """
        return render(request, 'register.html', {'register_errmsg': ''})

    def post(self, request):
        """
        实现用户注册
        :param request: 请求对象
        :return: 注册结果
        """
        # 接收前端表单数据,使用Post.get()方法
        username = request.POST.get('ussename')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        allow = request.POST.get('allow')
        image_code = request.POST.get('image_code')
        # 判断参数是否齐全
        if not all([username, password, password2, mobile, allow, image_code]):
            # all方法,对于列表或元祖内的任意一个元素为false,则返回false,空            列表或空元祖或任意元素不为false,则返回Ture
            # 数据不合法返回错误参赛
            return http.HttpResponseForbidden("缺少必传参数")
        # 判断用户名是否是5-20个字符
        if not re.match(r"^[a-zA-Z0-9_-]{5,20}$", username):
            return http.HttpResponseForbidden("请输入5-20个字符的用户名")
        # 判断密码是否是8 - 20个数字
        if not re.match(r"^[a-zA-Z0-9]{8,20}$", password):
            return http.HttpResponseForbidden("请输入8-20位的密码")
        # 判断两次密码是否一致
        if password != password2:
            return http.HttpResponseForbidden('两次输入的密码不一致')
        # 判断手机号是否合法
        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return http.HttpResponseForbidden('请输入正确的手机号码')
        # 判断是否勾选用户协议
        if allow != "on":
            return http.HttpResponseForbidden('请勾选用户协议')
        # 保存注册数据
        try:
            user = UserInfo.objects.create_user(
                username=username, password=password, mobile=mobile)
        except DatabaseError:
            return render(request, 'register.html', {'register_errmsg': '注册失败'})

        # 登入用户，实现状态保持
        login(request, user)

        # 响应注册结果
        # return http.HttpResponse('注册成功，重定向到首页')
        # 正常登录时返回首面,从用户中心退出再登录时返回用户中心页面，关键字参数为?next=/login/
        response = redirect('/')  # SESSION_COOKIE_AGE的值为2周
        response.set_cookie('username', user.username, max_age=14 * 24 * 3600)
        return response


class UsernameCountView(View):
    """检测用户名是否重复"""

    def get(self, request, username):
        # 查询数据库中是否有同名的用户，并返回Json数据格式
        count = UserInfo.objects.filter(username=username).count()
        return http.JsonResponse({'error_message': "ok", "code": RETCODE.OK, "count": count, })


class MobileCountView(View):
    """检测手机号码是否重复"""

    def get(self, request, mobile):
        count = UserInfo.objects.filter(mobile=mobile).count()
        return http.JsonResponse({'error_massage': "ok", 'code': RETCODE.OK, "count": count, })


class LoginView(View):
    """用户名登录"""

    def get(self, request):
        """
        提供登录界面
        :param request: 请求对象
        :return: 登录界面
        """
        return render(request, 'index.html', {'account_errmsg': ''})

    def post(self, request):
        """
        实现登录逻辑
        """
        # 接受参数
        username = request.POST.get('username')
        password = request.POST.get('password')
        remembered = request.POST.get('r')
        # 认证登录用户
        user = authenticate(username=username, password=password)
        print(user)
        if user is None:
            return render(request, 'index.html', {'account_errmsg': '用户名或密码错误'})
            # return JsonResponse(data)

        # 实现状态保持
        login(request, user)
        # 设置状态保持的周期
        if remembered != "1":
            request.session.set_expiry(0)
        # 没有记住用户：浏览器会话结束就过期, 默认是两周
        # request.session.set_expiry(0)

        # 响应登录结果
        # return redirect(reverse('contents:index'))
        response = redirect(request.GET.get('next', '/'))
        response.set_cookie('username', user.username, max_age=(
            14 * 24 * 3600 if remembered else None))
        return response
