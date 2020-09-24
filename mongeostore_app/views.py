'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-08-26 18:15:34
LastEditors: henggao
LastEditTime: 2020-09-24 22:49:52
'''
# from django.views.decorators.http import require_http_methods
# # from django.core import serializers
# from . import serializers
# from django.http import JsonResponse
# import json
# from .models import Mysegy
# import random
# from utils.tencent.sms import send_sms_single
# from mongeostore_v1 import settings
# import re
# from django.contrib.auth import authenticate, login
# from django.db import DatabaseError
# from django.shortcuts import HttpResponse, redirect, render
# from django import http
# from django.urls import reverse
# from django.views import View
# from mongeostore_app.models import UserInfo
# from utils.response_code import RETCODE

# Create your views here.


# @require_http_methods(['GET'])
# def add_segy(request):
#     response = {}
#     try:
#         segy = Mysegy(num_id=request.GET.get('num_id'))
#         segy.save()
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1

#     return JsonResponse(response)


# @require_http_methods(['GET'])
# def show_segys(request):
#     response = {}
#     try:
#         segys = Mysegy.objects.filter()
#         response['list'] = json.loads(serializers.serialize("json", segys))
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1

#     return JsonResponse(response)

# 发送短信验证


# def send_sms(request):
#     '''发送短信
#         ?tpl=login  -> 611307
#         ?tpl=register -> 611200

#     '''
#     tpl = request.GET.get('tpl')
#     template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
#     if not template_id:
#         return HttpResponse('模板不存在')

#     code = random.randrange(1000, 9999)
#     res = send_sms_single('15351818127', template_id, [code, ])
#     if res['result'] == 0:
#         return HttpResponse('成功')
#     else:
#         return HttpResponse(res['errmsg'])


#####   mongeostore 注册 ######
# class RegisterView(View):
#     """用户注册"""

#     def get(self, request):
#         """
#         提供注册界面
#         :param request: 请求对象
#         :return: 注册界面
#         """
#         return render(request, 'index.html', {'register_errmsg': ''})

#     def post(self, request):
#         """
#         实现用户注册
#         :param request: 请求对象
#         :return: 注册结果
#         """
#         # 接收前端表单数据,使用Post.get()方法
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         password2 = request.POST.get('password2')
#         mobile = request.POST.get('mobile')
#         email = request.POST.get('email')
#         allow = request.POST.get('allow')
#         image_code = request.POST.get('image_code')
#         # 判断参数是否齐全
#         if not all([username, password, password2, mobile, allow, image_code]):
#             # all方法,对于列表或元祖内的任意一个元素为false,则返回false,空            列表或空元祖或任意元素不为false,则返回Ture
#             # 数据不合法返回错误参赛
#             return http.HttpResponseForbidden("缺少必传参数")
#         # 判断用户名是否是5-20个字符
#         if not re.match(r"^[a-zA-Z0-9_-]{5,20}$", username):
#             return http.HttpResponseForbidden("请输入5-20个字符的用户名")
#         # 判断密码是否是8 - 20个数字
#         if not re.match(r"^[a-zA-Z0-9]{8,20}$", password):
#             return http.HttpResponseForbidden("请输入8-20位的密码")
#         # 判断两次密码是否一致
#         if password != password2:
#             return http.HttpResponseForbidden('两次输入的密码不一致')
#         # 判断手机号是否合法
#         if not re.match(r'^1[3-9]\d{9}$', mobile):
#             return http.HttpResponseForbidden('请输入正确的手机号码')
#         # 判断是否勾选用户协议
#         if allow != "on":
#             return http.HttpResponseForbidden('请勾选用户协议')
#         # 保存注册数据
#         try:
#             user = UserInfo.objects.create_user(
#                 username=username, password=password, mobile=mobile,email = email)
#         except DatabaseError:
#             return render(request, 'index.html', {'register_errmsg': '注册失败'})

#         # 登入用户，实现状态保持
#         login(request, user)

#         # 响应注册结果
#         # return http.HttpResponse('注册成功，重定向到首页')
#         # 正常登录时返回首面,从用户中心退出再登录时返回用户中心页面，关键字参数为?next=/login/
#         response = redirect('/')  # SESSION_COOKIE_AGE的值为2周
#         response.set_cookie('username', user.username, max_age=14 * 24 * 3600)
#         return response


# class UsernameCountView(View):
#     """检测用户名是否重复"""

#     def get(self, request, username):
#         # 查询数据库中是否有同名的用户，并返回Json数据格式
#         count = UserInfo.objects.filter(username=username).count()
#         return http.JsonResponse({'error_message': "ok", "code": RETCODE.OK, "count": count, })


# class MobileCountView(View):
#     """检测手机号码是否重复"""

#     def get(self, request, mobile):
#         count = UserInfo.objects.filter(mobile=mobile).count()
#         return http.JsonResponse({'error_massage': "ok", 'code': RETCODE.OK, "count": count, })

# class MobileCountView(View):
#     """检测邮箱是否重复"""

#     def get(self, request, email):
#         count = UserInfo.objects.filter(email=email).count()
#         return http.JsonResponse({'error_massage': "ok", 'code': RETCODE.OK, "count": count, })

# class LoginView(View):
#     """用户名登录"""

#     def get(self, request):
#         """
#         提供登录界面
#         :param request: 请求对象
#         :return: 登录界面
#         """
#         return render(request, 'index.html', {'account_errmsg': ''})

#     def post(self, request):
#         """
#         实现登录逻辑
#         """
#         # 接受参数
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         remembered = request.POST.get('r')
#         # 认证登录用户
#         user = authenticate(username=username, password=password)
#         print(user)
#         if user is None:
#             return render(request, 'index.html', {'account_errmsg': '用户名或密码错误'})
#             # return JsonResponse(data)

#         # 实现状态保持
#         login(request, user)
#         # 设置状态保持的周期
#         if remembered != "1":
#             request.session.set_expiry(0)
#         # 没有记住用户：浏览器会话结束就过期, 默认是两周
#         # request.session.set_expiry(0)

#         # 响应登录结果
#         # return redirect(reverse('contents:index'))
#         response = redirect(request.GET.get('next', '/'))
#         response.set_cookie('username', user.username, max_age=(
#             14 * 24 * 3600 if remembered else None))
#         return response


# from rest_framework.views import APIView
# from .models import StudentsModel
# from .serializers import StudentsSerializer
# class StudentsView(APIView):

#     def get(self, request):
#         queryset = StudentsModel.objects.all()
#         serializer = StudentsSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         data = request.data
#         serializer = StudentsSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

#     def put(self, request):
#         data = request.data
#         obj_id = data.pop('id')
#         instance = StudentsModel.objects.get(id=obj_id)
#         print("======================", instance.content)
#         serializer = StudentsSerializer(instance, data=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

## mongeostore ##
# import viewsets
import datetime
import pymongo
from pymongo import MongoClient
from django.core.exceptions import ValidationError
from django.contrib.auth import login
from django.db import DatabaseError
import re
from django.http.response import HttpResponse
from utils.tencent.sms import send_sms_single
import random
from mongeostore_v1 import settings
from django.shortcuts import redirect, render
from django.views import View
from django import http
from utils.response_code import RETCODE
from rest_framework import viewsets
# import local data
from .serializers import UserInfoSerializer
from .models import UserInfo
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from utils import encrypt
# create a viewset


class UserInfoViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = UserInfo.objects.all()

    # specify serializer to be used
    serializer_class = UserInfoSerializer


# class RegisterView111(View):
#     """
#     注册视图
#     /users/register
#     """

#     def get(self, request):
#         """
#         凡是来访问这个视图的请求, 就返回注册页面
#         :param request: 请求注册页面
#         :return: 注册页面
#         """
#         return render(request, 'index.html')
#     '添加注册用户'

#     def post(self, request):
#         # 1>校验数据
#         form = UserInfoSerializer(request.POST)
#         if form.is_valid():
#             # 2>创建数据
#             # username = form.cleaned_data.get('username')
#             # email = form.cleaned_data.get('email')
#             # password = form.cleaned_data.get('password')
#             # mobile = form.cleaned_data.get('mobile')
#             # UserInfo.objects.create_user(username=username, password=password, email=email,mobile=mobile)

#              # 接收前端表单数据,使用Post.get()方法
#             username = request.POST.get('username')
#             email = request.POST.get('email')
#             password = request.POST.get('password')
#             password2 = request.POST.get('password2')
#             mobile = request.POST.get('mobile')
#             smscode = request.POST.get('smscode')
#             allow = request.POST.get('allow')
#             # image_code = request.POST.get('image_code')

#             # 判断参数是否齐全
#             if not all([username, email, password, password2, mobile, allow, smscode]):
#                 # all方法,对于列表或元祖内的任意一个元素为false,则返回false,空            列表或空元祖或任意元素不为false,则返回Ture
#                 # 数据不合法返回错误参赛
#                 return http.HttpResponseForbidden("缺少必传参数")
#             # 判断用户名是否是5-20个字符
#             if not re.match(r"^[a-zA-Z0-9_-]{5,20}$", username):
#                 return http.HttpResponseForbidden("请输入5-20个字符的用户名")
#             # 判断邮箱
#             if not re.match(r"^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$", email):
#                 return http.HttpResponseForbidden("请输入有效邮箱")
#             # 判断密码是否是8 - 20个数字
#             if not re.match(r"^[a-zA-Z0-9_-]{6,20}$", password):
#                 return http.HttpResponseForbidden("请输入6-20位的密码")
#             # 判断两次密码是否一致
#             if password != password2:
#                 return http.HttpResponseForbidden('两次输入的密码不一致')
#             # 判断手机号是否合法Info
#             if not re.match(r'^1[3-9]\d{9}$', mobile):
#                 return http.HttpResponseForbidden('请输入正确的手机号码')
#             # 判断是否勾选用户协议
#             if allow != "on":
#                 return http.HttpResponseForbidden('请勾选用户协议')
#             # 保存注册数据
#             try:
#                 userInfo = UserInfo.objects.create_user(
#                     username=username, email=email, password=password, mobile=mobile)
#             except DatabaseError:
#                 return render(request, 'register.html', {'register_errmsg': '注册失败'})

#             # 登入用户，实现状态保持
#             login(request, userInfo)

#             # 响应注册结果
#             # return http.HttpResponse('注册成功，重定向到首页')
#             # 正常登录时返回首面,从用户中心退出再登录时返回用户中心页面，关键字参数为?next=/login/
#             response = redirect('/')  # SESSION_COOKIE_AGE的值为2周
#             response.set_cookie(
#                 'username', userInfo.username, max_age=14 * 24 * 3600)
#             # return response
#             # return json_response(errmsg='恭喜你,注册成功!')
#             return http.JsonResponse({'error_massage': "ok", 'code': RETCODE.OK, "UserInfo": UserInfo, })

#         else:
#             # 引发的错误可能会有多条错误信息,如果出错了,就将表单的报错信息进行拼接,
#             err_msg_list = []
#             for item in form.errors.values():
#                 # 遍历的item也是一个列表, 其中的第一个元素是报错信息
#                 err_msg_list.append(item[0])
#             err_msg_str = '/'.join(err_msg_list)
#             # 由于是参数错误, 所以使用Code.PARAMERR
#             # return json_response(errno=Code.PARAMERR, errmsg=err_msg_str)
#             return http.JsonResponse({'code': RETCODE.OK, "UserInfo": UserInfo, }, errmsg=err_msg_str)


# class UsernameCountView(View):
#     """检测用户名是否重复"""

#     def get(self, request, username):
#         # 查询数据库中是否有同名的用户，并返回Json数据格式
#         count = UserInfo.objects.filter(username=username).count()
#         return http.JsonResponse({'error_message': "ok", "code": RETCODE.OK, "count": count, })


# 发送短信验证


# def send_sms(request):
#     '''发送短信
#         ?tpl=login  -> 611307
#         ?tpl=register -> 611200

#     '''
#     tpl = request.GET.get('tpl')
#     template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
#     mobile = request.GET.get("mobile")
#     print(mobile)
#     print(tpl)
#     if not template_id:
#         return HttpResponse('模板不存在')

#     code = random.randrange(1000, 9999)
#     res = send_sms_single(mobile, template_id, [code, ])
#     if res['result'] == 0:
#         return HttpResponse('成功')
#     else:
#         return HttpResponse(res['errmsg'])

class CheckUsername(View):
    def get(self,request):
        #1.根据用户名，查询用户数量
        username = self.request.GET.get('username')  # 字符串类型
        count = UserInfo.objects.filter(username = username).count()

        #2. 返回响应
        data = {
            "count":count
        }
        print(data)
        return http.JsonResponse(data)




class MobileCountView(View):

    """检测短信模板是否有问题"""

    def get(self, request):
        tpl = self.request.GET.get('tpl')
        print(tpl)
        template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
        if not template_id:
            raise ValidationError("短信模板错误")

        """检测手机号码是否重复"""
        mobile = self.request.GET.get('mobile')  # 字符串类型
        # print(type(mobile)) #字符串类型str
        # count = UserInfo.objects.filter(mobile=mobile).count()
        # return http.JsonResponse({'error_massage': "ok", 'code': RETCODE.OK, "count": count, })
        if UserInfo.objects.filter(mobile=mobile).count():
            raise ValidationError("手机号已经注册过，请重新输入")

        #生成短信验证码
        code = random.randrange(1000, 9999)

        # 发送短信
        sms = send_sms_single(mobile, template_id, [code, ])
        if sms["result"] != 0:
            raise ValidationError("短信发送失败，{}".format['errmsg'])

        # 验证码写入mongodb
        '''
        MongoDB 2.2 引入一个新特性–TTL 集合，TTL集合支持失效时间设置，或者在某个特定时间;

        集合自动清除超时文档，者用来保存一个诸如session会话信息的时候非常有用。

        如果想使用TTL集合，用用到 expireAfterSeconds 选项.
        '''
        client = MongoClient("192.168.55.110", 27017)
        collection = client.mobilecode.expire
        collection.create_index(
            [("time", pymongo.ASCENDING)], expireAfterSeconds=66)
        data = {
            "mobile": mobile,  # 注意这个存入的类型，这样传入的是字符串str
            "code": code,
        }
        collection.insert(data)
        return http.JsonResponse({'error_massage': "ok", 'code': RETCODE.OK, })


class RegisterView(View):
    """
      注册视图
      /users/register
      """
    # @method_decorator(ensure_csrf_cookie)

    def get(self, request):
        """
        凡是来访问这个视图的请求, 就返回注册页面
        :param request: 请求注册页面
        :return: 注册页面
        """
        # return render(request, 'index.html')
        print(request.POST)
        return http.JsonResponse({'error_massage': "ok", 'code': RETCODE.OK, })

    # '添加注册用户'
    # @method_decorator(ensure_csrf_cookie)
    def post(self, request):
        # 1>校验数据
        # form = UserInfoSerializer(request.POST)

        # 2>创建数据
        # 接收前端表单数据,使用Post.get()方法
        username = self.request.POST.get('username')
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')
        password2 = self.request.POST.get('password2')  # 前端已经校验了
        mobile = self.request.POST.get('mobile')
        smscode = self.request.POST.get('smscode')
        # allow = request.POST.get('allow') #是否同意协议
        print(username)
        print(email)
        print(password)
        print(mobile)
        print(password2)
        print(smscode)  # 2916"}
        # 为了防止爬虫，后端需要再一次校验信息
        # 判断参数是否齐全
        if not all([username, email, password, password2, mobile, smscode]):
            # all方法,对于列表或元祖内的任意一个元素为false,则返回false,空            列表或空元祖或任意元素不为false,则返回Ture
            return http.HttpResponseForbidden("缺少必传参数")

        """检测用户名是否重复"""
        if not re.match(r"^[a-zA-Z0-9_-]{5,20}$", username):
            return http.HttpResponseForbidden("请输入5-20个字符的用户名")
        if UserInfo.objects.filter(username=username).count():
            raise ValidationError("该用户名已经注册过，请重新输入")

        """检测邮箱是否重复"""
        if not re.match(r"^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$", email):
            return http.HttpResponseForbidden("请输入有效邮箱")
        if UserInfo.objects.filter(email=email).count():
            raise ValidationError("该邮箱已经注册过，请重新输入")
        """检测密码"""
        #  判断密码是否是6 - 20个数字
        if not re.match(r"^[a-zA-Z0-9_-]{6,20}$", password):
            return http.HttpResponseForbidden("请输入6-20位的密码")
            # 判断两次密码是否一致
        if password != password2:
            return http.HttpResponseForbidden('两次输入的密码不一致')
        md5_password = encrypt.md5(password)  # 使用MD5密文
        print("密文密码：" + md5_password)

        """检测手机号"""
        # 判断手机号是否合法Info
        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return http.HttpResponseForbidden('请输入正确的手机号码')
        if UserInfo.objects.filter(mobile=mobile).count():
            raise ValidationError("该手机已经注册过，请重新输入")

        """检测验证码"""
        client = MongoClient("192.168.55.110", 27017)
        collection = client.mobilecode.expire
        code_mobile = self.request.POST.get("mobile")
        print(type(code_mobile))  # str
        print(code_mobile)
        mongo_code = collection.find_one({"mobile": code_mobile})
        # {'_id': ObjectId('5f6317893f3884e0759155a0'), 'mobile': '15351818127', 'code': 4891}
        print(mongo_code)
        if not mongo_code:
            raise ValidationError("验证码失效，或未发送，请重新发送！")
        mongo_str_code = str(mongo_code['code'])
        print(mongo_str_code)  # 4981
        print(type(mongo_str_code))  # <class 'str'>
        print(smscode)
        print(type(smscode))  # <class 'str'>
        # 这个验证码还有点问题，申请的腾讯一天只能10条
        if smscode != mongo_str_code:
            raise ValidationError("验证码错误，请重新输入")
        # 保存注册数据
        try:
            userInfo = UserInfo.objects.create(
                username=username, email=email, password=md5_password, mobile=mobile)
        except DatabaseError:
            return render(request, 'index.html', {'register_errmsg': '注册失败'})

        return HttpResponse('welcome!{}'.format(username))
        # return username
