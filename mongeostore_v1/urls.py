'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-08-26 16:59:36
LastEditors: henggao
LastEditTime: 2020-08-27 21:20:40
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
from django.contrib import admin
from django.urls import path
import mongeostore_app.urls
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(mongeostore_app.urls)),
]
