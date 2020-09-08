'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-08-26 16:59:36
LastEditors: henggao
LastEditTime: 2020-09-08 20:08:30
'''
"""mongeostore_v1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from mongeostore_app import views
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, re_path
import mongeostore_app.urls
from django.conf.urls import url, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('send/sms/', views.send_sms),
    path('api/', include(mongeostore_app.urls)),
    path('', TemplateView.as_view(template_name="index.html")),
    # mongeostore #
    # path('register/', views.register),
    # re_path(r'.*', TemplateView.as_view(template_name='index.html'))
    re_path(r'.*', TemplateView.as_view(template_name='index.html')),
    
    path('captcha/', include('captcha.urls'))   # 增加这一行
]
