'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-07 17:22:57
LastEditors: henggao
LastEditTime: 2020-10-14 08:48:09
'''
file = ".\mongeostore_env\mytest\LX_SEGY2.segy"

file_type = file.split(".")[-1]
print(file_type)
file_name = file.split("\\")[-1]
print(file_name)