'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-09-28 11:03:19
LastEditors: henggao
LastEditTime: 2021-05-11 21:55:44
'''
import segyio

content = ".\mongeostore_env\mytest\LX_SEGY2.segy"
# content = ".\mongeostore_env\mytest\mytest.SGY"
with segyio.open(content, mode="r", strict=False, ignore_geometry=False, endian='big') as f:
    # print(f.trace)  # Trace(traces = 255701, samples = 2001)
    # print(f.tracecount)  # 255701
    # print(len(segyio.tools.collect(f.trace[:]))) #255701
    print(f.header[0]) #道头
    # print(f.header[1])
    # b = f.header[0]
    # print(type(b))
    # c = str(b)
    # print(c)
    # print(type(c))
    # print(f.bin)
    # print(f.text)
    # print(segyio.tools.collect(f.trace[:]))
    # [    0.         0.         0.     ... -7441.8984 -4465.1406 -1488.3799]
    # print(f.trace[255700])
    # print(type(f.trace[0]))
    # a= f.trace[0]
    # b = a.tolist()
    # print(b)
    # print(type(b))
    # <generator object Trace.__getitem__.<locals>.gen at 0x00000215242258C8>
    # print(f.trace[:])
    # print(len(f.trace[0])) #2001
    # print(f.header[0])
    # print(segyio.BinField.Traces)
    # print(f.header[17])
    # print(f.ilines)
    # print(f.xlines)
    # print(f.xline)
    # print(f.trace[300])
    # print(f.trace[300][1500])
    


ff = open(r".\mongeostore_env\mytest\LX_SEGY2.segy")
print(ff.name)
print(ff.read(5))
ff.close()