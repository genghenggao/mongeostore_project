'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-23 21:47:34
LastEditors: henggao
LastEditTime: 2020-11-18 14:59:44
'''
import time
import collections
import re
from bson.objectid import ObjectId
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
from .models import FileInfo
from rest_framework.views import APIView
from .serializers import FileInfoSerializer
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

# 展示Data.vue表格数据
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


#################树形结构对应分内容######################


#################树形结构对应分内容######################
