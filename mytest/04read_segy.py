'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-11 16:39:26
LastEditors: henggao
LastEditTime: 2020-10-14 20:38:04
'''
import segyio
from gridfs import GridFS
from bson.objectid import ObjectId
import pymongo
from pymongo import MongoClient
import gridfs

######example 查询数据库下所有collection名称########
client = MongoClient("192.168.55.110", 20000)
db = client['segyfile']
coll_names = db.list_collection_names(session=None)
# print(coll_names)  # ['LX_SEGY', 'LX_SEGY2', 'fs.files', 'fs.chunks', 'User']


# 使用segyio读取segy文件
fs = client.segyfile.mysegy.chunks
filename = client.segyfile.mysegy.files
# print(fs.find())  # <pymongo.cursor.Cursor object at 0x00000143A18F0CC8>

# print(filename.find())  # <pymongo.cursor.Cursor object at 0x00000143A18F0CC8>

db = client.grid
fs_gridfs = gridfs.GridFS(db)
files = fs_gridfs.find()
files_segy = fs_gridfs.find_one({"md5": "2105ca42eba2041fa4bca6030944ae89"})
# print(files)  # <gridfs.grid_file.GridOutCursor object at 0x000002633B4983C8>
# print(files_segy)  # None

db2 = client.segyfile
filename2 = GridFS(db2, collection="mysegy")

# print(filename2)
# print(filename2.find({"filename": "AWS.png"}))
for cursor in filename2.find({"filename": "mytest.SGY"}):
    print(cursor.filename)
    # filenname = cursor.LX_SEGY2.segy
    if cursor.filename == "mytest.SGY":
        filename = cursor.filename
        # content = cursor.read()
        with open(filename, "wb") as f:
            content = cursor.read()
            f.write(content)
   
    # file = ".\mongeostore_env\mytest\mytest.SGY"
    with segyio.open(cursor.filename, mode="rb", strict=False, ignore_geometry=False, endian='big') as f:
        print(f.tracecount)

        f.close()
