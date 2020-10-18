'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-09-28 11:03:19
LastEditors: henggao
LastEditTime: 2020-10-15 09:58:01
'''
import segyio

content = ".\mongeostore_env\mytest\LX_SEGY2.segy"
# content = ".\mongeostore_env\mytest\mytest.SGY"
with segyio.open(content, mode="r", strict=False, ignore_geometry=False, endian='big') as f:
    # print(f.tracecount)
    # print(f.bin)
    # print(f.text)
    print(segyio.tools.collect(f.trace[:]))
    # print(f.trace[0])
    # print(f.header[0])