'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-11-22 16:04:04
LastEditors: henggao
LastEditTime: 2020-11-30 23:09:46
'''
# coding=utf-8

from datetime import datetime
import time

t = "Wed Nov 04 2020 00:00:00 GMT+0800 (CST)"
# print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t)))


dd = "Fri Nov 09 2018 14:41:35 GMT+0800 (CST)"
GMT_FORMAT = '%a %b %d %Y %H:%M:%S GMT+0800 (CST)'
# print(datetime.strptime(t, GMT_FORMAT))

#coding:UTF-8
import time

timestamp = 1462451334

#转换成localtime
time_local = time.localtime(timestamp)
#转换成新的时间格式(2016-05-05 20:28:54)
dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)

print (dt)
