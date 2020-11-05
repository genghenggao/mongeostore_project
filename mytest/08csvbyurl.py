'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-11-04 08:52:02
LastEditors: henggao
LastEditTime: 2020-11-04 08:59:04
'''
import requests
import csv
from contextlib import closing

'''
通过url读取csv
'''
# 文件地址
url = "http://snk-gm.hz.37.com.cn/downloads/rankshow/20191205/snk_Rugal_1006_44_1575532733_COST_MONEY_20191204050000.csv"

# 读取数据
with closing(requests.get(url, stream=True)) as r:
    f = (line.decode('gbk') for line in r.iter_lines())
    reader = csv.reader(f, delimiter=',', quotechar='"')
    for row in reader:
        print(row)
