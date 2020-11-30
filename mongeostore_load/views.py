'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-23 21:47:34
LastEditors: henggao
LastEditTime: 2020-11-30 22:56:02
'''
from rest_framework import viewsets
import base64
from django.http.request import HttpRequest
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
import time
import collections
import re
from bson.objectid import ObjectId
from rest_framework.response import Response
import xlrd
import csv
from bson.json_util import dumps
from django.core import serializers
from django.http import request
from django.http.response import HttpResponseNotAllowed, JsonResponse
from django.views.decorators.http import condition, require_http_methods
from gridfs import GridFS
import os
from django.http import response
from xlrd.formula import colname
from .models import DrillInclinationModel, DrillMetaModel, FileInfo
from rest_framework.views import APIView
from .serializers import DrillInclinationSerializer, DrillMetaSerializer, FileInfoSerializer
from typing import ClassVar
from django.http import HttpResponse
from django.shortcuts import render
import pymongo
import gridfs
import json
from pymongo.mongo_client import MongoClient

# Create your views here.


def uploadfile(request, *args, **kwargs):
    """
    docstring
    """
    # print("Hello Uploader")
    #  上传文件到gridfs
    # client = mongo_client("192.168.55.110", 20000)  # 连接MongoDB数据库
    # db = client.segyfile  # 选定数据库，设定数据库名称为segyfile
    # print(db)
    data = {
        "uuid": "dasdsadsa",
        "status": 0,
    }
    if request.method == "POST":
        myFile = request.FILES.get("id", None)  # 获取上传的文件，如果没有文件，则默认为None
        # print("经过这里")
        # print(myFile)
        # img_type = os.path.splitext(img_obj.name)[1]  # .jpg  获取文件名后缀
        if not myFile:
            print("经过这里啊")
            return HttpResponse("no files for upload!")
        return HttpResponse("test!")
    else:
        print("那就经过这里哈")
        # return Response("success!")

        # with open(myFile, 'rb') as f:
        #     data = f.read()
        #     fs = gridfs.GridFS(db, 'mysegy')  # 连接GridFS集合，名称位mysegy
        #     fs.put(data)
        #     # return fs.put(data)
        # return HttpResponse(json.dumps(response_data), content_type="application/json")

    # return HttpResponse(data)
    return HttpResponse("You are better")

# 上传到GriDFS数据，UploadFile.vue


class FileInfoView(APIView):

    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        # print("走的是GET方法")
        response = {}
        queryset = FileInfo.objects.all()
        serializer_class = FileInfoSerializer
        response['code'] = 200
        # response["Access-Control-Allow-Methods"] = "POST"
        return HttpResponse(json.dumps(response), content_type="application/json")

    def post(self, request):
        """
        docstring
        """
        # print("走的是POST方法")
        # file = self.request.POST.get('name',None)  # 获取上传的文件，如果没有文件，则默认为None
        File = request.FILES.get("file", None)  # 注意比较
        # print(File)
        # print(File.name)   #同上
        # print(File.chunks)  # 二进制信息
        _id = self.request.POST.get('id')
        filename = self.request.POST.get('filename')
        type = self.request.POST.get('type')
        size = self.request.POST.get('size')
        upload_date = self.request.POST.get('upload_date')
        publisher = self.request.POST.get('publisher')
        # print(filename)
        # print(publisher)

        # 保存到本地
        if not os.path.exists('upload/'):
            os.mkdir('upload/')
        with open("./upload/%s" % File.name, 'wb+') as f:
            for chunk in File.chunks():
                f.write(chunk)
            f.close()

        #  上传文件到MongoDB中gridfs
        client = MongoClient("192.168.55.110", 20000)  # 连接MongoDB数据库
        # 如果没有数据库，创建数据库
        db = client.segyfile  # 选定数据库，设定数据库名称为segyfile
        with open("./upload/%s" % File.name, 'rb') as f:
            _id = self.request.POST.get('id')
            filename = self.request.POST.get('filename')
            contentType = self.request.POST.get('type')
            size = self.request.POST.get('size')
            upload_date = self.request.POST.get('upload_date')
            publisher = self.request.POST.get('publisher')
            # print(upload_date)
            dic = {
                "_id": _id,
                "filename": filename,
                "contentType": contentType,
                "length": size,
                "uploadDate": upload_date,
                "publisher": publisher,
                "aliases": [publisher],  # 别名
                "metadata": filename,
            }
            data = f.read()
            fs = gridfs.GridFS(db, 'mysegy')  # 连接GridFS集合，名称位mysegy
            fs.put(data, **dic)
            f.close()
        client.close()
        return HttpResponse("Successful")

# 展示GridFS数据，SeiTable.vue
@require_http_methods(['GET'])
def FileShow(request):
    """
    docstring
    """
    client = MongoClient("192.168.55.110", 20000)  # 连接MongoDB数据库
    db = client.segyfile  # 选定数据库，设定数据库名称为segyfile
    fs = GridFS(db, collection='mysegy')  # 连接GridFS集合，名称为mysegy
    gf = fs.find_one()
    # print(gf.filename)
    # print(gf.length)
    # print(dir(gf.md5))
    # print(dir(gf.md5))

    response = {}
    data = []
    for grid_out in fs.find({"$where": "this._id.match(/.*o/)"}):
        # print(grid_out._file)
        # response = {}
        # response = grid_out._file
        response['uploadDate'] = str(grid_out.upload_date)
        # print(response)
        # print(type(response))
        # print(json.dumps(response))

        data.append(grid_out._file)
        # print(data)
        response['list'] = data
        response['msg'] = 'success'
        response['error_num'] = 0
    client.close()
    return JsonResponse(response, safe=False)  # 不加safe=False的话必须返回dic
    # return JsonResponse(json.loads(response)) #不加safe=False的话必须返回dict
    # return HttpResponse(json.dumps(response), content_type="application/json")

# 元数据下载
@require_http_methods(['GET'])
def filedownload(request):
    """
    docstring
    """
    client = MongoClient("192.168.55.110", 20000)  # 连接MongoDB数据库

    # file_id1 = request.FILES.get("_id", None)
    # file_id2 = request.POST.get("_id")
    file_id = request.GET.get("_id")
    # print(file_id1)
    # print(file_id2)
    # print(file_id)
    db = client.segyfile  # 选定数据库，设定数据库名称为segyfile
    fs = GridFS(db, collection='mysegy')  # 连接GridFS集合，名称为mysegy

    # 读取文件
    filetodown = fs.find_one({"$where": "this._id.match(/.*" + file_id + "/)"})
    # print(filetodown)
    # print(filetodown.name)
    # 下载文件
    File = filetodown.name
    content = filetodown.read()

    with open("../mongeostore_env/upload/%s" % File, 'wb') as f:
        f.write(content)
    client.close()
    return HttpResponse("success")
    # return render(request, 'http://localhost:8080/maincontent')

# 展示Data.vue表格数据
@require_http_methods(['GET'])
def ShowData(request):
    """
    docstring
    """
    client = pymongo.MongoClient("192.168.55.110", 20000)
    database = "segyfile"
    db = client[database]
    # 选择集合
    collection = "excel_data"
    db_coll = db[collection]
    # 查询
    content = {}
    datainfo = []
    for document in db_coll.find():

        # print(document)
        # print(type(document))
        # print(document.vip)
        # response['_id'] = str(document._id)
        datainfo.append(document)
        content = dumps(datainfo)  # 这个地方要用字符串传到前端去
        # return HttpResponse(json.dumps(document), content_type="application/json")
        # return json.loads(json_util.dumps(document))
        # print(type(content))
    client.close()
    return HttpResponse(content, "application/json")

# 解析csv文件到数据库


class UploadCSV(APIView):
    """
    docstring
    """

    def get(self, request):
        """
        docstring
        """
        File = request.FILES.get("file", None)

        return HttpResponse(File)
    # @require_http_methods(['POST'])

    def post(self, request):
        """
        docstring
        """
        # 从前端拿到数据
        File = request.FILES.get("file", None)
        # 保存到本地
        if not os.path.exists('upload/'):
            os.mkdir('upload/')
        with open("./upload/%s" % File.name, 'wb+') as f:
            for chunk in File.chunks():
                f.write(chunk)
            f.close()
        # 写入mongodb，data数据库
        client = pymongo.MongoClient("192.168.55.110", 20000)
        database = "segyfile"
        db = client[database]
        collection = "data"
        db_coll = db[collection]

        with open("./upload/%s" % File.name, 'r', encoding='utf-8')as csvfile:
            # 调用csv中的DictReader函数直接获取数据为字典形式
            reader = csv.DictReader(csvfile)
            # 创建一个counts计数一下 看自己一共添加了了多少条数据
            counts = 0
            for each in reader:
                # 将数据中需要转换类型的数据转换类型。原本全是字符串（string）。
                each['?rank'] = int(each['?rank'])
                each['costMoney'] = float(each['costMoney'])
                each['combat'] = float(each['combat'])
                each['topHeroesCombat'] = int(each['topHeroesCombat'])
                # each['表显里程'] = float(each['表显里程'])
                # each['排量'] = float(each['排量'])
                # each['过户数量'] = int(each['过户数量'])
                db_coll.insert(each)
                # set1.insert_one(each)
                counts += 1
                # print('成功添加了'+str(counts)+'条数据 ')
        client.close()
        return HttpResponse("uploadcsv success")

# 上传Excel到数据库（自动转为json）


class UploadExcel(APIView):
    """
    docstring
    """

    def get(self, request):
        """
        docstring
        """
        File = request.FILES.get("file", None)

        return HttpResponse(File)
    # @require_http_methods(['POST'])

    def post(self, request):
        """
        docstring
        """
        # 从前端拿到数据
        File = request.FILES.get("file", None)
        # 保存到本地
        if not os.path.exists('upload/'):
            os.mkdir('upload/')
        with open("./upload/%s" % File.name, 'wb+') as f:
            for chunk in File.chunks():
                f.write(chunk)
            f.close()
        # 写入mongodb，data数据库
        client = pymongo.MongoClient("192.168.55.110", 20000)
        database = "segyfile"
        db = client[database]
        collection = "excel_data"
        db_coll = db[collection]

        # 读取Excel文件
        data = xlrd.open_workbook("./upload/%s" % File.name)
        table = data.sheets()[1]
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
            db_coll.insert(returnData[i])
        client.close()
        return HttpResponse("uploadexcel success")


def EditData(request):
    if request.method == "POST":

        # 1、通过——id拿到前端数据,这样取不到值，用request.body
        # data_id = request.POST.get("_id")
        # print(data_id)
        # s使用request.POST取值
        # all_data = request.POST
        # print(all_data)
        # <QueryDict: {'{"json_data":"{\\"_id\\":{\\"$oid\\":\\"5fa7dc070a6d3e479de148d9\\"},\\"ZK_num\\":\\"ZK1\\",\\"Depth\\":0,\\"Azimuth\\":131.29,\\"Inclination\\":-86.4}"}': ['']}>
        # 使用request.body取值
        body_data = request.body
        # print(body_data)
        # b'{"json_data":"{\\"_id\\":{\\"$oid\\":\\"5fa7dc070a6d3e479de148d9\\"},\\"ZK_num\\":\\"ZK1\\",\\"Depth\\":0,\\"Azimuth\\":131.29,\\"Inclination\\":-86.4}"}'
        data_json = json.loads(body_data)
        # {'json_data': '{"_id":{"$oid":"5fa7dc070a6d3e479de148d9"},"ZK_num":"ZK1","Depth":0,"Azimuth":131.29,"Inclination":-86.4}'}
        # print(data_json)
        # print(data_json.values())
        # print(data_json['json_data']) #{"_id":{"$oid":"5fa7dc070a6d3e479de148d9"},"ZK_num":"ZK1","Depth":"1","Azimuth":131.29,"Inclination":-86.4}
        query_data_json = data_json['json_data']
        # print(type(query_data_json)) #<class 'str'>

        dict_data = json.loads(query_data_json)
        # {'_id': {'$oid': '5fa7dc070a6d3e479de148d9'}, 'ZK_num': 'ZK1', 'Depth': '1', 'Azimuth': 131.29, 'Inclination': -86.4}
        # print(dict_data)
        # print(type(dict_data))  # <class 'dict'>
        front_query_oid = dict_data['_id']
        # print(front_query_oid)  # {'$oid': '5fa7dc070a6d3e479de148d9'}
        # print(type(front_query_oid))  # <class 'dict'>
        front_query_id = front_query_oid['$oid']
        # print(front_query_id)  # 5fa7dc070a6d3e479de148d9   终于拿到了！！
        # print(type(front_query_id))  # <class 'str'>
        # 连接数据库
        client = pymongo.MongoClient("192.168.55.110", 20000)
        database = "segyfile"
        db = client[database]
        collection = "excel_data"
        db_coll = db[collection]
        # 根据_id匹配到后端数据
        cursor = db_coll.find_one(filter={"_id": ObjectId(front_query_id)})
        # {'_id': ObjectId('5fa7dc070a6d3e479de148d9'), 'ZK_num': 'ZK1', 'Depth': 0.0, 'Azimuth': 131.29, 'Inclination': -86.4}
        # print(cursor)

        # 删掉_'_id': {'$oid': '5fa7dc070a6d3e479de148d9'}部分
        dict_data.pop('_id')
        # {'ZK_num': 'ZK1', 'Depth': 0, 'Azimuth': 131.29, 'Inclination': -86.4}
        # print(dict_data)
        # print(type(dict_data))  # <class 'dict'>
        update_data = db_coll.update_one(
            cursor, update={"$set": dict_data})
        # print(update_data)
        # print(update_data.matched_count)
        # print(update_data.modified_count)
        # 关闭连接
        client.close()
    return HttpResponse('success')

# 删除数据


def DeleteData(request):
    """
    Delete data
    """
    if request.method == "POST":
        body_data = request.body
        # print(body_data)
        data_json = json.loads(body_data)
        query_data_json = data_json['json_data']
        dict_data = json.loads(query_data_json)
        front_query_oid = dict_data['_id']
        front_query_id = front_query_oid['$oid']
        # print(front_query_id)

        # 连接数据库
        client = pymongo.MongoClient("192.168.55.110", 20000)
        database = "segyfile"
        db = client[database]
        collection = "excel_data"
        db_coll = db[collection]

        db_coll.remove({"_id": ObjectId(front_query_id)})
        # print("Delete Success")
        # 关闭连接
        client.close()

    return HttpResponse("Delete Success")


def AddData(request):
    """
    docstring
    """
    if request.method == "POST":
        body_data = request.body
        print(type(body_data))  # <class 'bytes'>
        data_json = json.loads(body_data)
        print(type(data_json))  # <class 'dict'>
        query_data_json = data_json['tmp_data']
        print(type(query_data_json))
        # 将数据类型转换一下
        query_data_json['Depth'] = float(query_data_json['Depth'])
        query_data_json['Azimuth'] = float(query_data_json['Azimuth'])
        query_data_json['Inclination'] = float(query_data_json['Inclination'])
        print(query_data_json)

        # 连接数据库
        client = pymongo.MongoClient("192.168.55.110", 20000)
        database = "segyfile"
        db = client[database]
        collection = "excel_data"
        db_coll = db[collection]

        result = db_coll.insert_one(document=query_data_json)
        print("添加成功 Success")
        # 关闭连接
        # client.close()

    return HttpResponse("Delete Success")

#  collection数据搜索


def QueryData(request):
    """
    docstring
    """
    if request.method == "POST":

        body_data = request.body  # b'{"ZK_num_data":"ZK1"}'
        data_json = json.loads(body_data)
        ZK_num = data_json['ZK_num_data']

        # 连接数据库
        client = pymongo.MongoClient("192.168.55.110", 20000)
        database = "segyfile"
        db = client[database]
        collection = "excel_data"
        db_coll = db[collection]
        # 根据字段匹配到后端数据
        datainfo = []
        content = {}
        cursors = db_coll.find({"ZK_num": ZK_num})
        for cursor in cursors:
            datainfo.append(cursor)
            content = dumps(datainfo)
        # print(content)
        client.close()
        return HttpResponse(content, "application/json")


def ShowDataBase(request):
    """
    获取数据库以及集合，在前端实现展示
    """
    if request.method == "GET":
        # 连接mongoDB数据库
        client = pymongo.MongoClient("192.168.55.110", 20000)
        # 查询数据库
        # ['admin', 'config', 'gridfs', 'segyfile', 'testGridfs', 'testdb', '中文数据库']
        databases = client.list_database_names()
        databases.remove('admin')
        databases.remove('config')
        database_total = len(databases)  # 获取数据库个数

        # print("=========================================")
        list_db = []
        # children = []
        dict_db = {}
        dict_col = {}
        children_id = database_total
        database_id = 0
        content = {}
        for database in databases:
            children = []
            cur_database = client[database]
            collections = cur_database.list_collection_names()
            # 删除.files和.chunks文件
            # print("===================当前在的数据库是：" + str(database))
            for collection in collections:
                # print(collection)
                # 删除.chunks集合
                if ('.chunks') in collection:
                    collections.remove(collection)
            # print(collections)

            for collection in collections:
                # print(collection)
                # 删.files集合
                if ('.files') in collection:
                    collections.remove(collection)
            # print(collections)

            # 将数据按前端数据要求存放
            for collection in collections:
                children_id += 1
                dict_col = {
                    'id': children_id,
                    'label': collection,
                    'isEdit': False,  # 主要用于前端判断添加、修改、删除按钮
                    '_database': database,  # 属于哪个数据库，后续便于修改集合名称
                }
                children.append(dict_col)
            # print(children)
            database_id += 1
            dict_db = {
                'id': database_id,
                'label': database,
                'isEdit': True,  # 主要用于前端判断添加、修改、删除按钮
                'children': children
            }
            list_db.append(dict_db)
            content = dumps(list_db)  # 这个地方要用字符串传到前端去
        # print(content)
        # print(type(content))
        # print(list_db)
        # print(type(list_db))
        return HttpResponse(content, "application/json")
        # return HttpResponse('success')


def EditDataBase(request):
    """
    docstring
    """
    if request.method == "POST":
        editdatas = request.body
        edit_json = json.loads(editdatas)
        # print(edit_json)
        # print(edit_json['value'])
        new_databasename = edit_json['value']  # 新名称
        data = edit_json['data']
        # print(data['isEdit'])

        # 连接mongoDB数据库，读取 db 库 table 表中的数据
        client = pymongo.MongoClient("192.168.55.110", 20000)
        if (data['isEdit']):
            check_name = data['label']  # 数据库名称
            # print(check_name)
            # start_time = time.time()
            old_database = client[check_name]  # 获取数据库
            # 新的数据库，下面三行创建一个临时集合，这样创建一个新的数据库
            new_database = client[new_databasename]
            temp_collection = new_database[new_databasename]
            temp_collection.insert_one({})
            collection_list = old_database.list_collection_names()
            for item in collection_list:
                query = {
                    'renameCollection': check_name + '.' + item,
                    'to': new_databasename + '.' + item
                }
                client.admin.command(query)
            # print(time.time() - start_time)
            # 删除临时集合
            temp_collection.drop()
            # 删除原来的数据库
            client.drop_database(old_database)

            # client.admin.command(
            #     'copydb', fromdb=check_name, todb=new_databasename)
        else:
            # 1.判断集合在哪个数据库
            check_database = data['_database']  # 拿到数据库名称
            # print(check_database)
            db = client[check_database]  # 取到数据库
            # 2. 集合的名称
            old_collection_name = data['label']  # 拿到l老的集合名称
            # print(new_collection)
            # print(type(new_collection))
            # 3. 拿到集合，适用复制的方式
            old_collection = db[old_collection_name]  # 取到老的集合
            # new_collection = db[new_databasename]  # 新的集合
            # new_collection_name = old_collection.rename(new_collection) #不支持分片集群的集合修改

            # 使用MongoDB Aggregation运算符$match和$out
            pipeline = [{"$match": {}},
                        {"$out": new_databasename},
                        ]
            old_collection.aggregate(pipeline)

            # 删除原来的集合
            # old_collection.remove({}) #清空文档
            old_collection.drop()  # 删除集合

    return HttpResponse('success')


def AddDataBase(parameter_list):
    """
    add a mongodb database
    """
    pass


def DeleteDataBase(request):
    """
    delete a mongodb database
    """
    pass


def AddCollection(request):
    """
    docstring
    """
    if request.method == "POST":
        body_data = request.body
        # print(body_data)
        data_json = json.loads(body_data)
        print(data_json)
        data = data_json['newChild']
        col_name = data['label']  # 取到集合名称
        print(col_name)
        data_name = data['_database']  # 取到数据库名称

        # 连接mongoDB数据库，读取 db 库 table 表中的数据
        client = pymongo.MongoClient("192.168.55.110", 20000)
        db = client[data_name]  # 连接数据库
        collections = db.list_collection_names()
        if col_name in collections:
            # 后端再次判断集合是否存在
            print('数据库存在')
            return HttpResponse('集合已经存在')
        else:
            # 创建集合
            db.create_collection(col_name)
            return HttpResponse('success')


def DeleteCollection(request):
    """
    delete a mongodb collection
    """
    if request.method == "POST":
        body_data = request.body
        # print(body_data)
        data_json = json.loads(body_data)
        # print(data_json)
        data = data_json['data']
        col_name = data['label']  # 取到集合名称
        data_name = data['_database']  # 取到数据库名称

        # 连接mongoDB数据库，读取 db 库 table 表中的数据
        client = pymongo.MongoClient("192.168.55.110", 20000)
        db = client[data_name]  # 连接数据库
        collections = db.list_collection_names()
        if col_name in collections:
            # 删除集合
            db[col_name].drop()
            print('删除成功')

        return HttpResponse('success')


#################MonGeoStore######################

# 自定义分页类，实现分页功能
# 创建分页类
class MyPagination(PageNumberPagination):
    page_size = 10  # 每页显示数据的数量

    max_page_size = 100   # 每页最多可以显示的数据数量

    page_query_param = 'currentPage'  # 获取页码时用的参数,当前页码

    page_size_query_param = 'PageSize'  # 调整每页显示数量的参数名，每页数据大小

    # 指定返回格式，根据需求返回一个总页数，数据存在results字典里返回

    def get_paginated_response(self, data):
        """重写get_paginated_response方法"""

        tpl = {
            'count': self.page.paginator.count,  # 总条数
            'links': {
                'next': self.get_next_link(),  # 下一页
                'previous': self.get_previous_link()  # 上一页
            }
        }
        tpl.update(data)  # 重新定义模板
        res = {
            'data': tpl,
            'retCode': 0,
            'retMsg': u"成功 | Success"
        }
        # 通过渲染器进行返回
        return Response(res)


# 钻孔数据管理子系统---测斜表Inclination分页

class DrillInclinationPageView(APIView):
    def get(self, request, *args, **kwargs):
        # 数据获取，使用using('drill')需要在settings.py中配置
        # print(request.GET)

        # page_size = request.GET['PageSize']
        # print(page_size)
        drill_obj = DrillInclinationModel.objects.using(
            'drill').all().order_by('_id')  # 一定要排序
        # totalcount = drill_obj.count()  # 总数据数
        # 创建分页对象
        # print(drill_obj)
        page = MyPagination()
        # 实例化查询，获取分页的数据
        page_chapter = page.paginate_queryset(
            queryset=drill_obj, request=request, view=self)
        # print(page_chapter)
        # 序列化及结果返回，将分页后返回的数据, 进行序列化
        ser = DrillInclinationSerializer(instance=page_chapter, many=True)
        # print(ser)
        data = {'list': ser.data}
        # print(ser.data)
        # print(data)
        # data = page.get_paginated_response(ser.data)
        # print(data)
        # 自定义的分页类中实例化后使用get_paginated_response方法可以实现显示上下页链接的功能
        # return data   #使用DRF测试http:/r/127.0.0.1:8000/load/drillinclination/
        # 转换成json格式, ensure_ascii=False 表示显示中文, 默认为True
        # ret = json.dumps(ser.data, ensure_ascii=False)
        # print(ret)
        # return HttpResponse(ret, "application/json")
        return page.get_paginated_response(data)


# 钻孔数据管理子系统---测斜表Inclination搜索
class InclinationSearchView(APIView):
    def get(self, request, *args, **kwargs):
        # 数据获取，使用using('drill')需要在settings.py中配置
        print(request.GET)

        search_key = request.GET['ZK_num']  # 根据ZK_num字段搜索
        # print(page_size)
        drill_obj = DrillInclinationModel.objects.using(
            'drill').filter(ZK_num=search_key).all().order_by('_id')  # 一定要排序
        # totalcount = drill_obj.count()  # 总数据数
        # 创建分页对象
        page = MyPagination()
        search_class = filters.SearchFilter()
        # 需要搜索的字段
        self.search_fields = ['ZK_num']
        # 实例化搜索查询器
        search_query = search_class.filter_queryset(
            request, drill_obj, self)

        # 实例化查询，获取分页的数据
        page_chapter = page.paginate_queryset(
            queryset=search_query, request=request, view=self)
        # 序列化及结果返回，将分页后返回的数据, 进行序列化
        ser = DrillInclinationSerializer(instance=page_chapter, many=True)
        data = {'list': ser.data}
        return page.get_paginated_response(data)

# 钻孔数据管理子系统---元数据分页

# 钻孔元数据信息


# class DrillMetaViewSet(viewsets.ModelViewSet):
class DrillMetaViewSet(APIView):

    def get(self, request, *args, **kwargs):
        queryset = DrillMetaModel.objects.all()
        # queryset = InclinationMetaModel.objects.using('drill').all()
        serializer_class = DrillMetaSerializer

        # return HttpResponse(json.dumps(serializer_class), content_type="application/json")
        return HttpResponse(queryset)

    def post(self, request):
        """
        docstring
        """
        # print("走的是POST方法")
        # file = self.request.POST.get('name',None)  # 获取上传的文件，如果没有文件，则默认为None
        zk_histogram = request.FILES.get("file", None)  # 注意比较
        # print(File)
        # print(File.name)   #同上
        # print(File.chunks)  # 二进制信息
        print(request.data['upload_date'])  # DRF才有request.data
        print(request.POST)  # Django只有request.POST、request.GET
        _id = self.request.POST.get('id')
        zk_num = request.data['zk_num'],  # 取出来竟是个元组，QAQ
        zk_type = request.data['zk_type'],
        final_depth = request.data['final_depth'],
        final_date = request.data['final_date'],
        depth = request.data['depth'],
        project_name = request.data['project_name'],
        company_name = request.data['company_name'],
        uploader = request.data['uploader'],
        upload_date = request.data['uploaddate'],  # 这个字段前端会冲突，另起
        print(zk_num[0])
        print(final_depth[0])
        print(type(upload_date[0]))
        print(upload_date[0])
        print(final_date[0])

        # test = DrillMetaModel(zk_num='ZK1')
        # test.save()
        # # DrillMetaModel.objects.create(zk_num="ZK1")
        # DrillMetaModel.objects.create(_id=_id,
        #                               zk_num=zk_num[0],
        #                               zk_type=zk_type[0], final_depth=final_depth[0], final_date=final_date[0],
        #                               depth=depth[0],
        #                               project_name=project_name[0], company_name=company_name[0], uploader=uploader[0], upload_date=upload_date[0], zk_histogram=zk_histogram)
        # DrillMetaModel.objects.create(zk_type=zk_type[0])
        # DrillMetaModel.objects.create(final_depth=final_depth[0])
        # DrillMetaModel.objects.create(final_date=final_date[0])
        # DrillMetaModel.objects.create(depth=depth[0])
        # DrillMetaModel.objects.create(
        # project_name=project_name[0])
        # DrillMetaModel.objects.create(
        #     company_name=company_name[0])
        # DrillMetaModel.objects.create(uploader=uploader[0])
        # DrillMetaModel.objects.create(upload_date=upload_date[0])

        # DrillMetaModel.objects.create(
        #     zk_histogram=request.FILES.get("file", None))

        return HttpResponse('success')

# 钻孔数据管理子系统---测斜表Inclination删除


def DeleteInclination(request):
    """
    Delete data
    """
    if request.method == "POST":
        body_data = request.body
        # print(body_data)
        data_json = json.loads(body_data)
        query_data_json = data_json['json_data']
        dict_data = json.loads(query_data_json)
        front_query_oid = dict_data['_id']
        # front_query_id = front_query_oid['$oid']
        # print(front_query_id)
        # print(data_json['dbname'])

        # 连接数据库
        client = pymongo.MongoClient("192.168.55.110", 20000)
        # database = "segyfile"
        database = data_json['dbname']  # 从前端拿到数据库名称
        db = client[database]
        # collection = "excel_data"
        collection = data_json['colname']  # 从前端拿到数据库名称
        db_coll = db[collection]

        db_coll.remove({"_id": ObjectId(front_query_oid)})
        # print("Delete Success")
        # 关闭连接
        client.close()

    return HttpResponse("Delete Success")

# 钻孔数据管理子系统---测斜表Inclination删除


def EditInclination(request):
    if request.method == "POST":

        body_data = request.body

        data_json = json.loads(body_data)
        # print(data_json)

        query_data_json = data_json['json_data']

        dict_data = json.loads(query_data_json)

        front_query_oid = dict_data['_id']

        # front_query_id = front_query_oid['$oid']

        # 连接数据库
        client = pymongo.MongoClient("192.168.55.110", 20000)
        # print(data_json['colname'])
        # print(data_json['dbname'])
        # database = "segyfile"
        database = data_json['dbname']  # 从前端拿到数据库名称
        db = client[database]
        # collection = "excel_data"
        collection = data_json['colname']  # 从前端拿到集合名称
        db_coll = db[collection]
        # 根据_id匹配到后端数据
        cursor = db_coll.find_one(filter={"_id": ObjectId(front_query_oid)})
        # {'_id': ObjectId('5fa7dc070a6d3e479de148d9'), 'ZK_num': 'ZK1', 'Depth': 0.0, 'Azimuth': 131.29, 'Inclination': -86.4}
        # print(cursor)

        # 删掉_'_id': {'$oid': '5fa7dc070a6d3e479de148d9'}部分
        dict_data.pop('_id')
        # {'ZK_num': 'ZK1', 'Depth': 0, 'Azimuth': 131.29, 'Inclination': -86.4}
        # print(dict_data)
        # print(type(dict_data))  # <class 'dict'>
        update_data = db_coll.update_one(
            cursor, update={"$set": dict_data})
        # print(update_data)
        # print(update_data.matched_count)
        # print(update_data.modified_count)
        # 关闭连接
        client.close()
    return HttpResponse('success')

# 展示数据
@require_http_methods(['POST'])
def ShowCommonData(request):
    """
    docstring
    # """
    # db = request.GET.get('dbname')  # 获取到前端数据库名称
    # col_name = request.GET.get('colname')  # 获取到前端集合名称
    # print(request.body)
    body_data = request.body
    data_json = json.loads(body_data)
    print(data_json)
    db = data_json['dbname']  # 获取到前端数据库名称
    col_name = data_json['colname']  # 获取到前端集合名称
    # 连接数据库
    client = pymongo.MongoClient("192.168.55.110", 20000)
    db = client[db]
    db_coll = db[col_name]
    # # 查询
    content = {}
    datainfo = []
    for document in db_coll.find().limit(50):

        # print(document)
        # print(type(document))
        # print(document.vip)
        # response['_id'] = str(document._id)
        datainfo.append(document)
        content = dumps(datainfo)  # 这个地方要用字符串传到前端去
        # return HttpResponse(json.dumps(document), content_type="application/json")
        # return json.loads(json_util.dumps(document))
        # print(type(content))
    client.close()
    # print(content)
    return HttpResponse(content, "application/json")
    # return HttpResponse('content', "application/json")

# Collection数据修改


def CommonEditData(request):
    if request.method == "POST":

        body_data = request.body

        data_json = json.loads(body_data)
        # print(data_json)

        query_data_json = data_json['json_data']

        dict_data = json.loads(query_data_json)

        front_query_oid = dict_data['_id']

        front_query_id = front_query_oid['$oid']

        # 连接数据库
        client = pymongo.MongoClient("192.168.55.110", 20000)
        # print(data_json['colname'])
        # print(data_json['dbname'])
        # database = "segyfile"
        database = data_json['dbname']  # 从前端拿到数据库名称
        db = client[database]
        # collection = "excel_data"
        collection = data_json['colname']  # 从前端拿到集合名称
        db_coll = db[collection]
        # 根据_id匹配到后端数据
        cursor = db_coll.find_one(filter={"_id": ObjectId(front_query_id)})
        # {'_id': ObjectId('5fa7dc070a6d3e479de148d9'), 'ZK_num': 'ZK1', 'Depth': 0.0, 'Azimuth': 131.29, 'Inclination': -86.4}
        # print(cursor)

        # 删掉_'_id': {'$oid': '5fa7dc070a6d3e479de148d9'}部分
        dict_data.pop('_id')
        # {'ZK_num': 'ZK1', 'Depth': 0, 'Azimuth': 131.29, 'Inclination': -86.4}
        # print(dict_data)
        # print(type(dict_data))  # <class 'dict'>
        update_data = db_coll.update_one(
            cursor, update={"$set": dict_data})
        # print(update_data)
        # print(update_data.matched_count)
        # print(update_data.modified_count)
        # 关闭连接
        client.close()
    return HttpResponse('success')

# Collection数据删除


def CommonDeleteData(request):
    """
    Delete data
    """
    if request.method == "POST":
        body_data = request.body
        # print(body_data)
        data_json = json.loads(body_data)
        query_data_json = data_json['json_data']
        dict_data = json.loads(query_data_json)
        front_query_oid = dict_data['_id']
        front_query_id = front_query_oid['$oid']
        # print(front_query_id)
        # print(data_json['dbname'])

        # 连接数据库
        client = pymongo.MongoClient("192.168.55.110", 20000)
        # database = "segyfile"
        database = data_json['dbname']  # 从前端拿到数据库名称
        db = client[database]
        # collection = "excel_data"
        collection = data_json['colname']  # 从前端拿到数据库名称
        db_coll = db[collection]

        db_coll.remove({"_id": ObjectId(front_query_id)})
        # print("Delete Success")
        # 关闭连接
        client.close()

    return HttpResponse("Delete Success")


# Collection添加数据
def CommonAddData(request):
    """
    docstring
    """
    if request.method == "POST":
        body_data = request.body
        # print(type(body_data))  # <class 'bytes'>
        data_json = json.loads(body_data)
        # print(data_json['colname'])
        # print(type(data_json))  # <class 'dict'>
        query_data_json = data_json['tmp_data']
        # print(type(query_data_json))
        # print(query_data_json)

        # 由于公用集合，一些数据类型不知，所以这里默认使用字符串
        # 将数据类型转换一下
        # query_data_json['Depth'] = float(query_data_json['Depth'])
        # query_data_json['Azimuth'] = float(query_data_json['Azimuth'])
        # query_data_json['Inclination'] = float(query_data_json['Inclination'])
        # print(query_data_json)

        # 连接数据库
        client = pymongo.MongoClient("192.168.55.110", 20000)
        # database = "segyfile"
        database = data_json['dbname']
        db = client[database]
        # collection = "excel_data"
        collection = data_json['colname']
        db_coll = db[collection]

        result = db_coll.insert_one(document=query_data_json)
        print("添加成功 Success")
        # 关闭连接
        # client.close()

    return HttpResponse("Delete Success")

#  collection数据搜索

# Collection查询数据


def CommonQueryData(request):
    """
    docstring
    """
    if request.method == "POST":

        body_data = request.body  # b'{"ZK_num_data":"ZK1"}'
        data_json = json.loads(body_data)
        print(data_json)
        filter_key = data_json['filter_key_data']

        # 连接数据库
        client = pymongo.MongoClient("192.168.55.110", 20000)
        # database = "segyfile"
        database = data_json['dbname']
        db = client[database]
        # collection = "excel_data"
        collection = data_json['colname']
        db_coll = db[collection]
        # 根据字段匹配到后端数据
        listkeys = db_coll.find_one().keys()  # <class 'dict_keys'>
        second_key = list(listkeys)[1]  # 这里使用第二个字段进行查询

        datainfo = []
        content = {}
        cursors = db_coll.find({second_key: filter_key})
        for cursor in cursors:
            datainfo.append(cursor)
            content = dumps(datainfo)
        # print(content)
        client.close()
        return HttpResponse(content, "application/json")


# Excel数据上传到对应集合 CommonUploadExcel.vue


class CommonUploadExcel(APIView):
    """
    docstring
    """

    def get(self, request):
        """
        docstring
        """
        File = request.FILES.get("file", None)
        # print(request.data)

        return HttpResponse(File)
    # @require_http_methods(['POST'])

    def post(self, request):
        """
        docstring
        """
        # 从前端拿到数据
        File = request.FILES.get("file", None)
        # print('post')
        # print(request.data)
        # print(request.data['colname'])
        # print(request.data['dbname'])

        # 保存到本地
        if not os.path.exists('upload/'):
            os.mkdir('upload/')
        with open("./upload/%s" % File.name, 'wb+') as f:
            for chunk in File.chunks():
                f.write(chunk)
            f.close()
        # 写入mongodb，data数据库
        client = pymongo.MongoClient("192.168.55.110", 20000)
        # database = "segyfile"
        database = request.data['dbname']  # 从前端拿到数据库名称
        db = client[database]  # 连接数据库
        # collection = "excel_data"
        collection = request.data['colname']  # 从前端拿到数集合名称
        db_coll = db[collection]  # 连接集合

        # 读取Excel文件
        data = xlrd.open_workbook("./upload/%s" % File.name)
        list = data.sheet_names()  # 拿到EXcel的sheet名称
        if collection in list:
            print("yes")
            print(list.index(collection))  # 判断元素的位置
            x = list.index(collection)  # 获取集合的位置
        else:
            x = 0  # 不存在设置默认第一个sheet
        print(x)
        table = data.sheets()[x]
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
            db_coll.insert(returnData[i])
        client.close()
        return HttpResponse("uploadexcel success")


# 解析csv文件到数据库 CommonUploadCSV.vue
class CommonUploadCSV(APIView):
    """
    docstring
    """

    def get(self, request):
        """
        docstring
        """
        File = request.FILES.get("file", None)

        return HttpResponse(File)
    # @require_http_methods(['POST'])

    def post(self, request):
        """
        docstring
        """
        # 从前端拿到数据
        File = request.FILES.get("file", None)
        # 保存到本地
        if not os.path.exists('upload/'):
            os.mkdir('upload/')
        with open("./upload/%s" % File.name, 'wb+') as f:
            for chunk in File.chunks():
                f.write(chunk)
            f.close()
        # 写入mongodb，data数据库
        client = pymongo.MongoClient("192.168.55.110", 20000)
        # database = "segyfile"
        database = request.data['dbname']  # 从前端拿到数据库名称
        db = client[database]  # 连接数据库
        # collection = "excel_data"
        collection = request.data['colname']  # 从前端拿到数集合名称
        db_coll = db[collection]  # 连接集合

        with open("./upload/%s" % File.name, 'r', encoding='utf-8')as csvfile:
            # 调用csv中的DictReader函数直接获取数据为字典形式
            reader = csv.DictReader(csvfile)
            # 创建一个counts计数一下 看自己一共添加了了多少条数据
            counts = 0
            for each in reader:
                # 将数据中需要转换类型的数据转换类型。原本全是字符串（string）。
                each['?rank'] = int(each['?rank'])
                each['costMoney'] = float(each['costMoney'])
                each['combat'] = float(each['combat'])
                each['topHeroesCombat'] = int(each['topHeroesCombat'])
                # each['表显里程'] = float(each['表显里程'])
                # each['排量'] = float(each['排量'])
                # each['过户数量'] = int(each['过户数量'])
                db_coll.insert(each)
                # set1.insert_one(each)
                counts += 1
                # print('成功添加了'+str(counts)+'条数据 ')
        client.close()
        return HttpResponse("uploadcsv success")


# 上传源文件到GridFS数据库 CommonUploadMeta.vue
class CommonUploadMeta(APIView):

    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        # print("走的是GET方法")
        response = {}
        queryset = FileInfo.objects.all()
        serializer_class = FileInfoSerializer
        response['code'] = 200
        # response["Access-Control-Allow-Methods"] = "POST"
        return HttpResponse(json.dumps(response), content_type="application/json")

    def post(self, request):
        """
        docstring
        """
        # print("走的是POST方法")
        # file = self.request.POST.get('name',None)  # 获取上传的文件，如果没有文件，则默认为None
        File = request.FILES.get("file", None)  # 注意比较
        # print(File)
        # print(File.name)   #同上
        # print(File.chunks)  # 二进制信息
        _id = self.request.POST.get('id')
        filename = self.request.POST.get('filename')
        type = self.request.POST.get('type')
        size = self.request.POST.get('size')
        upload_date = self.request.POST.get('upload_date')
        publisher = self.request.POST.get('publisher')
        # print(filename)
        # print(publisher)

        # 保存到本地
        if not os.path.exists('upload/'):
            os.mkdir('upload/')
        with open("./upload/%s" % File.name, 'wb+') as f:
            for chunk in File.chunks():
                f.write(chunk)
            f.close()

        #  上传文件到MongoDB中gridfs
        client = MongoClient("192.168.55.110", 20000)  # 连接MongoDB数据库

        # 如果没有数据库，创建数据库
        # db = client.segyfile  # 选定数据库，设定数据库名称为segyfile
        # database = "segyfile"
        # print(request.data)
        database = request.data['colname']  # 从前端拿到数据库名称
        db = client[database]  # 连接数据库

        with open("./upload/%s" % File.name, 'rb') as f:
            _id = self.request.POST.get('id')
            filename = self.request.POST.get('filename')
            contentType = self.request.POST.get('type')
            size = self.request.POST.get('size')
            upload_date = self.request.POST.get('upload_date')
            publisher = self.request.POST.get('publisher')
            # print(upload_date)
            dic = {
                "_id": _id,
                "filename": filename,
                "contentType": contentType,
                "length": size,
                "uploadDate": upload_date,
                "publisher": publisher,
                "aliases": [publisher],  # 别名
                "metadata": filename,
            }
            data = f.read()
            fs = gridfs.GridFS(db, '元数据')  # 连接GridFS集合，名称为'元数据'
            fs.put(data, **dic)
            f.close()
        client.close()
        return HttpResponse("Successful")

# 展示GridFS数据，CommonMetaTable.vue
@require_http_methods(['GET'])
def CommonMetaShow(request):
    """
    docstring
    """
    client = MongoClient("192.168.55.110", 20000)  # 连接MongoDB数据库
    # print(request.GET.get('dbname'))
    dbname = request.GET.get('dbname')  # 从前端获取数据库名称
    # db = client.segyfile  # 选定数据库，设定数据库名称为segyfile
    db = client[dbname]  # 选定数据库
    fs = GridFS(db, collection='元数据')  # 连接GridFS集合，名称为元数据
    gf = fs.find_one()

    response = {}
    data = []
    for grid_out in fs.find({"$where": "this._id.match(/.*o/)"}):

        response['uploadDate'] = str(grid_out.upload_date)

        data.append(grid_out._file)
        # print(data)
        response['list'] = data
        response['msg'] = 'success'
        response['error_num'] = 0
    client.close()
    return JsonResponse(response, safe=False)  # 不加safe=False的话必须返回dic

# 下载元数据
@require_http_methods(['GET'])
def CommonFileDownload(request):
    """
    docstring
    """

    print(request.GET.get('dbname'))
    client = MongoClient("192.168.55.110", 20000)  # 连接MongoDB数据库

    file_id = request.GET.get("_id")
    db = request.GET.get('dbname')  # 获取数据库名称
    db = client[db]  # 选定数据库，设定数据库名称为segyfile
    fs = GridFS(db, collection='元数据')  # 连接GridFS集合，名称为元数据

    # 读取文件
    filetodown = fs.find_one({"$where": "this._id.match(/.*" + file_id + "/)"})

    # 下载文件
    File = filetodown.name
    content = filetodown.read()

    with open("../mongeostore_env/upload/%s" % File, 'wb') as f:
        f.write(content)
    client.close()
    return HttpResponse("success")
    # return render(request,"http://localhost:8080/mongeostore")


# 读取图片二进制流


def listAllImgFromDB(request):
    client = MongoClient("192.168.55.110", 20000)  # 连接MongoDB数据库
    db = client.segyfile  # 选定数据库，设定数据库名称为segyfile
    # db = client[dbname]  # 选定数据库
    fs = GridFS(db, collection='mysegy')  # 连接GridFS集合，名称为元数据

    file_id = 'o_1em6kq0js1jmsavl1n8q1nma2ock'
    # 读取文件
    image = fs.find_one({"$where": "this._id.match(/.*" + file_id + "/)"})
    # print(image.name)
    content = image.read()
    temp_data = base64.b64encode(content)  # 图片base64
    # print(temp_data)
    return HttpResponse(temp_data)


#################MonGeoStore######################
