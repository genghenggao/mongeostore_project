'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-11-05 19:25:23
LastEditors: henggao
LastEditTime: 2020-11-05 20:09:37
'''
import xlrd
import json
import pymongo

# 连接数据库

client = pymongo.MongoClient("192.168.55.110", 20000)
mydb = client['segyfile']
info = mydb['excel_data']
# 读取Excel文件
data = xlrd.open_workbook('./mongeostore_env/upload/data_w.xls')
# 选择上传的sheet，注意字段
table = data.sheets()[2]
# 读取excel第一行数据作为存入mongodb的字段名
rowstag = table.row_values(0)
nrows = table.nrows
returnData = {}


for i in range(1, nrows):
    # 将字段名和excel数据存储为字典形式，并转换为json格式
    returnData[i] = json.dumps(dict(zip(rowstag, table.row_values(i))))
    # 通过编解码还原数据
    returnData[i] = json.loads(returnData[i])
    print(returnData[i])
    info.insert(returnData[i])
