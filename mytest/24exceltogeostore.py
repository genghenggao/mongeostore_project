'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-12-06 22:10:13
LastEditors: henggao
LastEditTime: 2020-12-06 22:35:22
'''
import xlrd
import json
import pymongo

# 连接数据库

client = pymongo.MongoClient("192.168.55.110", 20000)
mydb = client['segyfile']
info = mydb['geo_data']
# 读取Excel文件
data = xlrd.open_workbook('./mongeostore_env/upload/01_metadata.xls')
# 选择上传的sheet，注意字段
# print(len(data.sheets())) #返回excel中sheet的数量
table = data.sheets()[0]
print(data.sheet_names())  # 拿到EXcel的sheet名称
list = data.sheet_names()  # 拿到EXcel的sheet名称
name = '定位表'
if name in list:
    print("yes")
    print(list.index(name))  # 判断元素的位置

# 读取excel第一行数据作为存入mongodb的字段名
rowstag = table.row_values(0)
# data1 = table.row_values(1)
# print(data1)
# print(rowstag[2])
nrows = table.nrows
# print(nrows)
returnData = {}


for i in range(1, nrows):
    data_x = table.row_values(i)[3]
    data_y = table.row_values(i)[4]
    coordinate = [data_x, data_y]
    returnData[i] = json.dumps(dict(zip(rowstag, table.row_values(i))))

    # 通过编解码还原数据
    returnData[i] = json.loads(returnData[i])
    returnData[i]['coordinate']=coordinate
    # print(returnData[i])
    info.insert(returnData[i])