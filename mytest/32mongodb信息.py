'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-12-27 20:53:29
LastEditors: henggao
LastEditTime: 2020-12-28 09:17:39
'''
from pymongo import MongoClient

######example 查询数据库下所有collection名称########
client = MongoClient("192.168.55.110", 20000)
db = client['钻孔数据管理子系统']
colname  = '定位表'
col = db.colname
# col = db[colname]
stats = db.command('collstats', '定位表')
# print(stats)
# print(stats['storageSize'] / 1024 / 1024)  # 获取占用硬盘的大小,#用 MB 作为单位
print(db)

# print(db.last_status)
# print (db.command("dbstats"))

# num = col.count_documents()  # 集合的count() 方法返回集合中文档的个数
# print(num)
# print(db.collection_names())