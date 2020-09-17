'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-09-17 15:17:57
LastEditors: henggao
LastEditTime: 2020-09-17 15:21:25
'''
'''密码加密'''

import hashlib

from django.conf import settings

def md5(string):
    '''MD5加密'''
    hash_object = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
    hash_object.update(string.encode('utf-8'))
    return hash_object.hexdigest()
