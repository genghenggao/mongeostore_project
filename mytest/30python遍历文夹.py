'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-12-20 17:24:40
LastEditors: henggao
LastEditTime: 2020-12-20 18:43:27
'''
#! /usr/bin/env python
# coding:utf-8

import os
import datetime

# base_dir = 'c:/'
base_dir = "./mongeostore_env/pic/"
list = os.listdir(base_dir)

filelist = []
for i in range(0, len(list)):
    path = os.path.join(base_dir, list[i])
    if os.path.isfile(path):
        filelist.append(list[i])

tabledata =[]
for i in range(0, len(filelist)):
    path = os.path.join(base_dir, filelist[i])
    if os.path.isdir(path):
        continue
    # 获取文件的修改时间
    timestamp = os.path.getmtime(path)
    print(timestamp)
    # 获取文件的修改时间
    ts1 = os.stat(path).st_mtime
    print(ts1)
    # 获取文件的大小,结果保留两位小数，单位为MB
    filesize = os.path.getsize(path)
    fsize = filesize/float(1024*1024)
    size = round(fsize, 2)
    filesize = str(size) + 'MB'
    print(size)

    date = datetime.datetime.fromtimestamp(timestamp)
    upload_time = date.strftime('%Y-%m-%d %H:%M:%S')
    # upload_time = date.strftime('%Y-%m-%d')
    # print(list[i], ' 最近修改时间是: ', date.strftime('%Y-%m-%d %H:%M:%S'))

    fileinfo = {
        'filename': list[i],
        'filesize': filesize,
        'upload_time': upload_time,
    }
    print(type(fileinfo))
    json_str = str(fileinfo)
    print(type(json_str))

    tabledata.append(json_str)
print(tabledata)