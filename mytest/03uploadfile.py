'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-13 21:39:22
LastEditors: henggao
LastEditTime: 2020-10-28 20:39:40
'''
#  上传文件到gridfs
import pymongo
import gridfs
from gridfs import GridFS
from bson import ObjectId
from pymongo.mongo_client import MongoClient
import datetime
client = MongoClient("192.168.55.110", 20000)  # 连接MongoDB数据库
db = client.segyfile  # 选定数据库，设定数据库名称为segyfile
fs = GridFS(db, collection='mysegy')  # 连接GridFS集合，名称为mysegy
# db = client['segyfile']
# @require_http_methods(['GET'])
print(db)
# 上传文件到GridFS集合中
# 存储文件到mongo

# file = ".\mongeostore_env\mytest\AWS.png"
file = ".\mongeostore_env\mytest\mytest.SGY"
# file = ".\mongeostore_env\mytest\LX_SEGY2.segy"


def upload():
    with open(file, 'rb') as f:

        file_type = file.split(".")[-1]
        # print(file_type)   #类型

        file_name = file.split("\\")[-1]
        # print(file_name)
        dic = {
            "filename": file_name,
            "contentType": file_type,
            "metadata": "test_name",
        }
        data = f.read()
        fs = gridfs.GridFS(db, 'mysegy')  # 连接GridFS集合，名称位mysegy
        # dic['上传时间'] = datetime.now()
        # content = open(path + filename, 'rb').read()  # 二进制格式读取文件内容
        fs.put(data, **dic)


def download():
    """
    docstring
    """
    # 下载文件
    for cursor in fs.find():
        print(cursor)
        File = cursor.filename
        content = cursor.read()
        with open("./mongeostore_env/upload/%s" % File, 'wb') as f:
            f.write(content)

if __name__ == '__main__':
    # upload()

    download()
