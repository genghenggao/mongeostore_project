'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-12-16 21:36:57
LastEditors: henggao
LastEditTime: 2021-04-13 20:07:41
'''
import gridfs
from mongeostore_v1 import settings
import base64
from bson.json_util import dumps
from django.test import client
from dwebsocket.decorators import accept_websocket, require_websocket
from functools import partial
import re
import numpy as np
import segyio
import datetime
import json
from django import http
from django.views.decorators.http import require_http_methods

from rest_framework import filters
from .serializers import RemoteInfoSerializer, SeiAcquisitionInfoSerializer, SeiInterpretationInfoSerializer, SeihistoricalInfoSerializer, SeiprocessInfoSerializer, SeismicInfoSerializer, LoggingInfoSerializer, GeologicalInfoSerializer, HydrologicalInfoSerializer
import os
from rest_framework.response import Response

from rest_framework.pagination import PageNumberPagination
from .models import RemoteInfo, SeiAcquisitionInfo, SeiInterpretationInfo, SeihistoricalInfo, SeiprocessInfo, SeismicInfo, LoggingInfo, GeologicalInfo, HydrologicalInfo
import time
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
# Create your views here.


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


class SeismicInfoView(APIView):
    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        seismic_obj = SeismicInfo.objects.all().order_by('_id')  # 一定要排序
        # print(seismic_obj)
        # 创建分页对象
        page = MyPagination()
        # 实例化查询，获取分页的数据
        page_chapter = page.paginate_queryset(
            queryset=seismic_obj, request=request, view=self)
        # 序列化及结果返回，将分页后返回的数据, 进行序列化
        ser = SeismicInfoSerializer(instance=page_chapter, many=True)
        data = {'list': ser.data}
        return page.get_paginated_response(data)

    def post(self, request, *args, **kwargs):
        """
        docstring
        """
        fileio = request.FILES.get("file", None)  # 注意比较

        # print(request.data['upload_date'])  # DRF才有request.data
        # print(request.POST)  # Django只有request.POST、request.GET
        # print(request.data)
        # _id = self.request.POST.get('id')
        seismic_filename = request.data['seismic_filename'],  # 取出来竟是个元组，QAQ
        location = request.data['location'],
        company_name = request.data['company_name'],
        uploader = request.data['uploader'],
        project_name = request.data['project_name'],
        seismic_upload_date = request.data['seismic_upload_date'],
        # 上传到GriDFS中
        filename = request.data['filename'],

        temp_time2 = int(seismic_upload_date[0])/1000
        # 转换成localtime
        time_local2 = time.localtime(temp_time2)
        # 转换成新的时间格式(2016-05-05 20:28:54)

        dt2 = time.strftime("%Y-%m-%d", time_local2)

        # 保存到本地
        if not os.path.exists('upload/'):
            os.mkdir('upload/')
        with open("./upload/%s" % fileio.name, 'wb+') as f:
            for chunk in fileio.chunks():
                f.write(chunk)
            f.close()
        # 写入数据
        write_data = SeismicInfo(
            seismic_filename=seismic_filename[0],
            location=location[0],
            project_name=project_name[0], company_name=company_name[0], uploader=uploader[0],
            seismic_upload_date=dt2)

        with open("./upload/%s" % fileio.name, 'rb') as fd:
            # 写入GridFS
            write_data.filedata.put(
                fd, content_type='segy', filename=seismic_filename[0], aliases=[filename[0]])
            # writedata.filedata.put(SeismicInfo, content_type='segy')
        write_data.save()

        return HttpResponse('success')

# 编辑地震元数据


def EditSeismicInfo(request):
    if request.method == "POST":

        body_data = request.body
        data_json = json.loads(body_data)
        # print(data_json)

        query_data_json = data_json['json_data']
        dict_data = json.loads(query_data_json)
        dict_data.pop('filedata')  # 去掉文件字段
        front_query_oid = dict_data['id']

        query_obj = SeismicInfo.objects.get(
            id=front_query_oid)
        print(query_obj)
        try:
            query_obj.update(**dict_data)
            query_obj.save()
            return HttpResponse('success')
        except:
            print('输入有误')
            status_code = 412
            return HttpResponse(status_code)


# 删除地震数据
def DeleteSeismicInfo(request):
    """
    docstring
    """
    if request.method == "POST":
        body_data = request.body
        # print(body_data)
        data_json = json.loads(body_data)
        # print(data_json)
        query_data_json = data_json['json_data']
        # print(query_data_json)
        dict_data = json.loads(query_data_json)
        print(dict_data)
        front_query_oid = dict_data['id']

        query_obj = SeismicInfo.objects.get(
            id=front_query_oid)
        print(query_obj)
        query_obj.delete()
        return HttpResponse("Delete Success")


class SeismicInfoSearch(APIView):
    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        # print('success')
        search_key = request.GET['search_key']  # 根据字段搜索
        # print(search_key)
        seismic_obj = SeismicInfo.objects.filter(
            seismic_filename=search_key).all().order_by('_id')  # 一定要排序
        # seismic_obj = SeismicInfo.objects.search_text(search_key).first()

        # 创建分页对象
        page = MyPagination()
        # 实例化查询，获取分页的数据
        page_chapter = page.paginate_queryset(
            queryset=seismic_obj, request=request, view=self)
        # 序列化及结果返回，将分页后返回的数据, 进行序列化
        ser = SeismicInfoSerializer(instance=page_chapter, many=True)
        data = {'list': ser.data}
        return page.get_paginated_response(data)


# 地震segy文件下载
@require_http_methods(['GET'])
def SeismicFileDownload(request):

    search_key = request.GET['file_id']  # 根据字段搜索
    print(search_key)

    # 从数据库拿到数据
    seismic_obj = SeismicInfo.objects(id=search_key).first()
    print(seismic_obj)
    print(seismic_obj.seismic_filename)
    filename = seismic_obj.seismic_filename
    seismic_file = seismic_obj.filedata.read()
    content_type = seismic_obj.filedata.content_type
    # print(type(seismic_file)) #<class 'bytes'>
    # print(type(content_type)) #<class 'str'>

    # 数据写入服务器
    with open("../mongeostore_env/upload/%s" % filename, 'wb') as f:
        f.write(seismic_file)
    print('save success')

    # # 拿到数据,返回前端
    with open("./upload/%s" % filename, "rb") as f:
        res = HttpResponse(f)
        res["Content-Type"] = "application/octet-stream"  # 注意格式
        res["Content-Disposition"] = 'filename="{}"'.format(filename)
    return res
    # return HttpResponse('success')


# 地震数据解析，获取文服务器件
@require_http_methods(['GET'])
def SeismicFileRead(request):

    # base_dir = 'c:/'
    base_dir = "././pic/"
    list = os.listdir(base_dir)

    filelist = []
    for i in range(0, len(list)):
        path = os.path.join(base_dir, list[i])
        if os.path.isfile(path):
            filelist.append(list[i])
    list_db = []
    content = {}
    for i in range(0, len(filelist)):
        path = os.path.join(base_dir, filelist[i])
        if os.path.isdir(path):
            continue
        # 获取文件的修改时间
        timestamp = os.path.getmtime(path)
        # print(timestamp)
        # 获取文件的修改时间
        # ts1 = os.stat(path).st_mtime
        # print(ts1)
        # 获取文件的大小,结果保留两位小数，单位为MB
        filesize = os.path.getsize(path)
        fsize = filesize/float(1024*1024)
        size = round(fsize, 2)
        filesize = str(size) + 'MB'
        # print(size)

        date = datetime.datetime.fromtimestamp(timestamp)
        upload_time = date.strftime('%Y-%m-%d %H:%M:%S')
        # upload_time = date.strftime('%Y-%m-%d')
        # print(list[i], ' 最近修改时间是: ', date.strftime('%Y-%m-%d %H:%M:%S'))

        fileinfo = {
            'filename': list[i],
            'filesize': filesize,
            'upload_time': upload_time,
        }
        # print(type(fileinfo))
        # json_str = str(fileinfo)
        # print(type(json_str))
        list_db.append(fileinfo)
        content = json.dumps(list_db)  # 这个地方要用字符串传到前端去
    # print(content)
    # print(type(content))
    return HttpResponse(content, "application/json")


# 地震数据解析，获取服务器文件
@require_http_methods(['GET'])
def SeismicHeaderQuery(request):
    print(request.GET)
    filename = request.GET.get('filename')
    filequery = request.GET.get('queryparams')
    filequerytype = request.GET.get('querytype')
    # print(filename)
    content = "..\mongeostore_env\pic\\" + filename

    try:
        with segyio.open(content, mode="r", strict=False, ignore_geometry=False, endian='big') as f:
            if filequery == 'header':
                datatest = f.header[0]
                queryinfo = str(datatest)
                return HttpResponse(queryinfo)
            elif filequery == 'Bin':
                datatest = f.bin
                queryinfo = str(datatest)
                return HttpResponse(queryinfo)
            elif filequery == 'track':
                datatest = f.text
                queryinfo = str(datatest)
                return HttpResponse(queryinfo)
            elif filequery == 'traces':
                datatest = f.trace
                queryinfo = str(datatest)
                return HttpResponse(queryinfo)
            elif filequery == 'trace1':
                datatest = f.trace[0]  # 拿到segy中数据
                # datatest = datatest.tolist()  #矩阵转列表
                queryinfo = str(datatest)
                # print(queryinfo)
                # print(type(queryinfo))
                return HttpResponse(queryinfo)
            elif filequery == 'trace1_view':
                datatest = f.trace[0]  # 拿到segy中数据
                datatest = datatest.tolist()  # 矩阵转列表
                queryinfo = str(datatest)
                # print(queryinfo)
                # print(type(queryinfo))
                return HttpResponse(queryinfo)
            elif filequery == 'trace_1':
                datatest = f.trace[-1]

                # print(str(datatest))
                queryinfo = str(datatest)
                return HttpResponse(queryinfo)
            elif filequery == 'trace_1_view':
                datatest = f.trace[-1]
                datatest = datatest.tolist()  # 矩阵转列表
                queryinfo = str(datatest)
                return HttpResponse(queryinfo)
            else:
                if filequerytype == 'text':
                    datatest = f.trace[int(filequery)]
                    # print(filequery)
                    # print(type(filequery))
                    # print(datatest)
                    queryinfo = str(datatest)
                    return HttpResponse(queryinfo)
                if filequerytype == 'views':
                    datatest = f.trace[int(filequery)]
                    datatest = datatest.tolist()  # 矩阵转列表
                    queryinfo = str(datatest)
                    return HttpResponse(queryinfo)
    except:
        print('解析错误')
        return HttpResponse('Sorry，查询失败~')

    # return HttpResponse('succes')
# 地震数据解析，获取服务器文件
@require_http_methods(['GET'])
def SeismicProfileQuery(request):
    # print(request.GET)
    filename = request.GET.get('filename')
    mtrace = request.GET.get('mtrace')
    ntrace = request.GET.get('ntrace')
    print(mtrace)
    # print(type(mtrace))
    print(ntrace)
    content = "..\mongeostore_env\pic\\" + filename

    try:
        with segyio.open(content, mode="r", strict=False, ignore_geometry=False, endian='big') as f:
            readdata = f.trace[int(mtrace):int(ntrace)]  # 读出generator object
            # datatest = data.tolist()  # 矩阵转列表
            data = []
            datajson = {}
            subdatalist = []
            for i in range(int(mtrace), int(ntrace)+1):
                outputdatalist = []

                # datatemp = f.trace[i].tolist()
                readdata = f.trace[i]
                # print(readdata)
                max_value = np.max(readdata)
                min_value = np.min(readdata)
                # print(max_value)
                # print(min_value)
                max_result = max_value if max_value > - \
                    min_value else -min_value  # 如果条件成立，将x的值赋给result
                # print(max_result)
                readdata = readdata/max_result+i
                n = -1
                for value in readdata:
                    n += 1
                    subdatalist = [n, value]
                    outputdatalist.append(subdatalist)

                data.append(outputdatalist)
                datajson = {
                    'data': data
                }

            return HttpResponse(str(datajson))
    except:
        print('解析错误')
        return HttpResponse('Sorry，查询失败~')


# 地震数据解析，获取整个地震剖面
@require_http_methods(['GET'])
def SeismicProfilePic(request):
    # print(request.GET)
    filename = request.GET.get('filename')
    # filequery = request.GET.get('queryparams')
    # filequerytype = request.GET.get('querytype')
    # print(filename)
    # 读取文件
    # image = "..\mongeostore_env\pic_seismic\\" + filename
    # client = MongoClient("192.168.55.110", 20000)  # 连接MongoDB数据库
    client = settings.MongoDB_cluster_client
    # db = client.segyfile  # 选定数据库，设定数据库名称为segyfile
    db = client['地震数据管理子系统']  # 选定数据库
    fs = gridfs.GridFS(db, collection='地震勘探数据')  # 连接GridFS集合，名称为元数据

    # file_id = 'o_1em6kq0js1jmsavl1n8q1nma2ock'
    file_name = 'LX_SEGY001.jpg'
    # 读取文件
    # image = fs.find_one({"$where": "this._id.match(/.*" + file_id + "/)"})
    image = fs.find_one(
        {"$where": "this.filename.match(/.*" + file_name + "/)"})
    # print(image.name)
    # 这里读取服务器中的数据
    # image = "..\mongeostore_env\pic_seismic\\" + 'LX_SEGY001.jpg'

    content = image.read()
    temp_data = base64.b64encode(content)  # 图片base64
    # print(temp_data)
    return HttpResponse(temp_data)


# 地震数据解析，删除服务器文件
@require_http_methods(['POST'])
def SeismicAnalysisDelete(request):
    # filename1 = request.POST
    # print(filename1)
    filename = request.POST.get('filename')
    print(filename)
    content = "..\mongeostore_env\pic\\" + filename
    os.remove(content)
    return HttpResponse('success')

# 地震数据解析，本地文件上传服务器


class SeismicAnalysisUpload(APIView):
    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        # print("走的是GET方法")
        response = {}
        response['code'] = 200
        # response["Access-Control-Allow-Methods"] = "POST"
        return HttpResponse(json.dumps(response), content_type="application/json")

    def post(self, request):
        File = request.FILES.get("file", None)
        # filename = request.POST.get('filename')
        # 保存到本地
        if not os.path.exists('pic/'):
            os.mkdir('pic/')
        with open("./pic/%s" % File.name, 'wb+') as f:
            for chunk in File.chunks():
                f.write(chunk)
            f.close()
        return HttpResponse('success')


# 地震数据解析，下载云端数据
# @require_http_methods(['GET'])
@accept_websocket
def AnalysisCloudDown(request):

    if request.is_websocket():  # 如果请求是websocket请求：

        WebSocket = request.websocket
        print(WebSocket)
        i = 0  # 设置发送至前端的次数
        messages = {}

        while True:
            i += 1  # 递增次数 i
            time.sleep(1)  # 休眠1秒

            # 判断是否通过websocket接收到数据
            if WebSocket.has_messages():

                # 存在Websocket客户端发送过来的消息
                client_msg = WebSocket.read().decode()
                print(client_msg)
                # # 从数据库拿到数据
                seismic_obj = SeismicInfo.objects(id=client_msg).first()
                filename = seismic_obj.seismic_filename
                seismic_file = seismic_obj.filedata.read  # 注意这个地方不用加（）
                seismic_filensize = seismic_obj.filedata.length
                content_type = seismic_obj.filedata.content_type
                filename = filename + '.' + content_type
                # 数据写入服务器
                RECORD_SIZE = 1024*40  # 单位是B
                with open("../mongeostore_env/pic/%s" % filename, 'wb') as f:
                    # f.write(seismic_file)
                    # print(f.tell())
                    # print('save success')
                    records = iter(partial(seismic_file, RECORD_SIZE), b'')
                    for r in records:
                        f.write(r)
                        percent = int(f.tell()*100/seismic_filensize)
                        # print(percent)
                        # print(percent)
                        # print(f.tell())
                        # return HttpResponse(percent)

                        # 设置发送前端的数据
                        messages = {
                            # 'time': time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time())),
                            # 'server_msg': 'send %d times!' % i,
                            'client_msg': client_msg,
                            'percent': percent
                        }
                        request.websocket.send(json.dumps(messages))
            # else:
            #     # 设置发送前端的数据
            #     messages = {
            #         'time': time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time())),
            #         'server_msg': 'send %d times!' % i,
            #     }

            #     # 设置发送数据为json格式
            #     request.websocket.send(json.dumps(messages))
    else:
        try:  # 如果是普通的http方法
            message = request.GET['message']
            return HttpResponse(message)
        except:
            # return render(request,'index.html')
            return HttpResponse('test123')


# 遥感数据上传
class RemoteInfoView(APIView):
    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        remote_obj = RemoteInfo.objects.all().order_by('_id')  # 一定要排序
        # print(seismic_obj)
        # 创建分页对象
        page = MyPagination()
        # 实例化查询，获取分页的数据
        page_chapter = page.paginate_queryset(
            queryset=remote_obj, request=request, view=self)
        # 序列化及结果返回，将分页后返回的数据, 进行序列化
        ser = RemoteInfoSerializer(instance=page_chapter, many=True)
        data = {'list': ser.data}
        return page.get_paginated_response(data)

    def post(self, request, *args, **kwargs):
        """
        docstring
        """
        fileio = request.FILES.get("file", None)  # 注意比较

        # print(request.data['upload_date'])  # DRF才有request.data
        # print(request.POST)  # Django只有request.POST、request.GET
        # print(request.data)
        # _id = self.request.POST.get('id')
        remote_filename = request.data['remote_filename'],  # 取出来竟是个元组，QAQ
        location = request.data['location'],
        company_name = request.data['company_name'],
        uploader = request.data['uploader'],
        project_name = request.data['project_name'],
        remote_upload_date = request.data['remote_upload_date'],
        # 上传到GriDFS中
        filename = request.data['filename'],

        temp_time2 = int(remote_upload_date[0])/1000
        # 转换成localtime
        time_local2 = time.localtime(temp_time2)
        # 转换成新的时间格式(2016-05-05 20:28:54)

        dt2 = time.strftime("%Y-%m-%d", time_local2)

        # 保存到本地
        if not os.path.exists('upload/'):
            os.mkdir('upload/')
        with open("./upload/%s" % fileio.name, 'wb+') as f:
            for chunk in fileio.chunks():
                f.write(chunk)
            f.close()
        # 写入数据
        write_data = RemoteInfo(
            remote_filename=remote_filename[0],
            location=location[0],
            project_name=project_name[0], company_name=company_name[0], uploader=uploader[0],
            remote_upload_date=dt2)

        with open("./upload/%s" % fileio.name, 'rb') as fd:
            # 写入GridFS
            write_data.filedata.put(
                fd, content_type='tif', filename=remote_filename[0], aliases=[filename[0]])
            # writedata.filedata.put(SeismicInfo, content_type='segy')
        write_data.save()

        return HttpResponse('success')


# 遥感数据编辑数据
def EditRemoteInfo(request):
    if request.method == "POST":

        body_data = request.body
        data_json = json.loads(body_data)
        # print(data_json)

        query_data_json = data_json['json_data']
        dict_data = json.loads(query_data_json)
        dict_data.pop('filedata')  # 去掉文件字段
        front_query_oid = dict_data['id']

        query_obj = RemoteInfo.objects.get(
            id=front_query_oid)
        print(query_obj)
        try:
            query_obj.update(**dict_data)
            query_obj.save()
            return HttpResponse('success')
        except:
            print('输入有误')
            status_code = 412
            return HttpResponse(status_code)

# 遥感数据删除数据


def DeleteRemoteInfo(request):
    """
    docstring
    """
    if request.method == "POST":
        body_data = request.body
        # print(body_data)
        data_json = json.loads(body_data)
        # print(data_json)
        query_data_json = data_json['json_data']
        # print(query_data_json)
        dict_data = json.loads(query_data_json)
        print(dict_data)
        front_query_oid = dict_data['id']

        query_obj = RemoteInfo.objects.get(
            id=front_query_oid)
        print(query_obj)
        query_obj.delete()
        return HttpResponse("Delete Success")

# 遥感数据查询数据


class RemoteInfoSearch(APIView):
    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        # print('success')
        search_key = request.GET['search_key']  # 根据字段搜索
        # print(search_key)
        remote_obj = RemoteInfo.objects.filter(
            remote_filename=search_key).all().order_by('_id')  # 一定要排序
        # seismic_obj = SeismicInfo.objects.search_text(search_key).first()

        # 创建分页对象
        page = MyPagination()
        # 实例化查询，获取分页的数据
        page_chapter = page.paginate_queryset(
            queryset=remote_obj, request=request, view=self)
        # 序列化及结果返回，将分页后返回的数据, 进行序列化
        ser = RemoteInfoSerializer(instance=page_chapter, many=True)
        data = {'list': ser.data}
        return page.get_paginated_response(data)


# 遥感数据下载数据
@require_http_methods(['GET'])
def RemoteFileDownload(request):

    search_key = request.GET['file_id']  # 根据字段搜索
    print(search_key)

    # 从数据库拿到数据
    remote_obj = RemoteInfo.objects(id=search_key).first()
    print(remote_obj)
    print(remote_obj.remote_filename)
    filename = remote_obj.remote_filename
    remote_file = remote_obj.filedata.read()
    content_type = remote_obj.filedata.content_type
    # print(type(seismic_file)) #<class 'bytes'>
    # print(type(content_type)) #<class 'str'>

    # 数据写入服务器
    with open("../mongeostore_env/upload/%s" % filename, 'wb') as f:
        f.write(remote_file)
    print('save success')

    # # 拿到数据,返回前端
    with open("./upload/%s" % filename, "rb") as f:
        res = HttpResponse(f)
        res["Content-Type"] = "application/octet-stream"  # 注意格式
        res["Content-Disposition"] = 'filename="{}"'.format(filename)
    return res
    # return HttpResponse('success')


# 测井数据上传
class LoggingInfoView(APIView):
    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        logging_obj = LoggingInfo.objects.all().order_by('_id')  # 一定要排序
        # print(seismic_obj)
        # 创建分页对象
        page = MyPagination()
        # 实例化查询，获取分页的数据
        page_chapter = page.paginate_queryset(
            queryset=logging_obj, request=request, view=self)
        # 序列化及结果返回，将分页后返回的数据, 进行序列化
        ser = LoggingInfoSerializer(instance=page_chapter, many=True)
        data = {'list': ser.data}
        return page.get_paginated_response(data)

    def post(self, request, *args, **kwargs):
        """
        docstring
        """
        fileio = request.FILES.get("file", None)  # 注意比较

        # print(request.data['upload_date'])  # DRF才有request.data
        # print(request.POST)  # Django只有request.POST、request.GET
        # print(request.data)
        # _id = self.request.POST.get('id')
        logging_filename = request.data['logging_filename'],  # 取出来竟是个元组，QAQ
        location = request.data['location'],
        company_name = request.data['company_name'],
        uploader = request.data['uploader'],
        project_name = request.data['project_name'],
        logging_upload_date = request.data['logging_upload_date'],
        # 上传到GriDFS中
        filename = request.data['filename'],

        temp_time2 = int(logging_upload_date[0])/1000
        # 转换成localtime
        time_local2 = time.localtime(temp_time2)
        # 转换成新的时间格式(2016-05-05 20:28:54)

        dt2 = time.strftime("%Y-%m-%d", time_local2)

        # 保存到本地
        if not os.path.exists('upload/'):
            os.mkdir('upload/')
        with open("./upload/%s" % fileio.name, 'wb+') as f:
            for chunk in fileio.chunks():
                f.write(chunk)
            f.close()
        # 写入数据
        write_data = LoggingInfo(
            logging_filename=logging_filename[0],
            location=location[0],
            project_name=project_name[0], company_name=company_name[0], uploader=uploader[0],
            logging_upload_date=dt2)

        with open("./upload/%s" % fileio.name, 'rb') as fd:
            # 写入GridFS
            write_data.filedata.put(
                fd, content_type='prn', filename=logging_filename[0], aliases=[filename[0]])
            # writedata.filedata.put(SeismicInfo, content_type='segy')
        write_data.save()

        return HttpResponse('success')


# 测井数据编辑数据
def EditLoggingInfo(request):
    if request.method == "POST":

        body_data = request.body
        data_json = json.loads(body_data)
        # print(data_json)

        query_data_json = data_json['json_data']
        dict_data = json.loads(query_data_json)
        dict_data.pop('filedata')  # 去掉文件字段
        front_query_oid = dict_data['id']

        query_obj = LoggingInfo.objects.get(
            id=front_query_oid)
        print(query_obj)
        try:
            query_obj.update(**dict_data)
            query_obj.save()
            return HttpResponse('success')
        except:
            print('输入有误')
            status_code = 412
            return HttpResponse(status_code)

# 测井数据删除数据


def DeleteLoggingInfo(request):
    """
    docstring
    """
    if request.method == "POST":
        body_data = request.body
        # print(body_data)
        data_json = json.loads(body_data)
        # print(data_json)
        query_data_json = data_json['json_data']
        # print(query_data_json)
        dict_data = json.loads(query_data_json)
        print(dict_data)
        front_query_oid = dict_data['id']

        query_obj = LoggingInfo.objects.get(
            id=front_query_oid)
        print(query_obj)
        query_obj.delete()
        return HttpResponse("Delete Success")

# 测井数据查询数据


class LoggingInfoSearch(APIView):
    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        # print('success')
        search_key = request.GET['search_key']  # 根据字段搜索
        # print(search_key)
        logging_obj = LoggingInfo.objects.filter(
            logging_filename=search_key).all().order_by('_id')  # 一定要排序
        # seismic_obj = SeismicInfo.objects.search_text(search_key).first()

        # 创建分页对象
        page = MyPagination()
        # 实例化查询，获取分页的数据
        page_chapter = page.paginate_queryset(
            queryset=logging_obj, request=request, view=self)
        # 序列化及结果返回，将分页后返回的数据, 进行序列化
        ser = LoggingInfoSerializer(instance=page_chapter, many=True)
        data = {'list': ser.data}
        return page.get_paginated_response(data)


# 测井数据下载数据
@require_http_methods(['GET'])
def LoggingFileDownload(request):

    search_key = request.GET['file_id']  # 根据字段搜索
    print(search_key)

    # 从数据库拿到数据
    logging_obj = LoggingInfo.objects(id=search_key).first()
    print(logging_obj)
    print(logging_obj.logging_filename)
    filename = logging_obj.logging_filename
    logging_file = logging_obj.filedata.read()
    content_type = logging_obj.filedata.content_type
    # print(type(seismic_file)) #<class 'bytes'>
    # print(type(content_type)) #<class 'str'>

    # 数据写入服务器
    with open("../mongeostore_env/upload/%s" % filename, 'wb') as f:
        f.write(logging_file)
    print('save success')

    # # 拿到数据,返回前端
    with open("./upload/%s" % filename, "rb") as f:
        res = HttpResponse(f)
        res["Content-Type"] = "application/octet-stream"  # 注意格式
        res["Content-Disposition"] = 'filename="{}"'.format(filename)
    return res
    # return HttpResponse('success')


# 地质数据上传
class GeologicalInfoView(APIView):
    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        geological_obj = GeologicalInfo.objects.all().order_by('_id')  # 一定要排序
        # print(seismic_obj)
        # 创建分页对象
        page = MyPagination()
        # 实例化查询，获取分页的数据
        page_chapter = page.paginate_queryset(
            queryset=geological_obj, request=request, view=self)
        # 序列化及结果返回，将分页后返回的数据, 进行序列化
        ser = GeologicalInfoSerializer(instance=page_chapter, many=True)
        data = {'list': ser.data}
        return page.get_paginated_response(data)

    def post(self, request, *args, **kwargs):
        """
        docstring
        """
        fileio = request.FILES.get("file", None)  # 注意比较

        # print(request.data['upload_date'])  # DRF才有request.data
        # print(request.POST)  # Django只有request.POST、request.GET
        # print(request.data)
        # _id = self.request.POST.get('id')
        # 取出来竟是个元组，QAQ
        geological_filename = request.data['geological_filename'],
        location = request.data['location'],
        company_name = request.data['company_name'],
        uploader = request.data['uploader'],
        project_name = request.data['project_name'],
        geological_upload_date = request.data['geological_upload_date'],
        # 上传到GriDFS中
        filename = request.data['filename'],

        temp_time2 = int(geological_upload_date[0])/1000
        # 转换成localtime
        time_local2 = time.localtime(temp_time2)
        # 转换成新的时间格式(2016-05-05 20:28:54)

        dt2 = time.strftime("%Y-%m-%d", time_local2)

        # 保存到本地
        if not os.path.exists('upload/'):
            os.mkdir('upload/')
        with open("./upload/%s" % fileio.name, 'wb+') as f:
            for chunk in fileio.chunks():
                f.write(chunk)
            f.close()
        # 写入数据
        write_data = GeologicalInfo(
            geological_filename=geological_filename[0],
            location=location[0],
            project_name=project_name[0], company_name=company_name[0], uploader=uploader[0],
            geological_upload_date=dt2)

        with open("./upload/%s" % fileio.name, 'rb') as fd:
            # 写入GridFS
            write_data.filedata.put(
                fd, content_type='jpeg/png', filename=geological_filename[0], aliases=[filename[0]])
            # writedata.filedata.put(SeismicInfo, content_type='segy')
        write_data.save()

        return HttpResponse('success')


# 地质数据编辑数据
def EditGeologicalInfo(request):
    if request.method == "POST":

        body_data = request.body
        data_json = json.loads(body_data)
        # print(data_json)

        query_data_json = data_json['json_data']
        dict_data = json.loads(query_data_json)
        dict_data.pop('filedata')  # 去掉文件字段
        front_query_oid = dict_data['id']

        query_obj = GeologicalInfo.objects.get(
            id=front_query_oid)
        print(query_obj)
        try:
            query_obj.update(**dict_data)
            query_obj.save()
            return HttpResponse('success')
        except:
            print('输入有误')
            status_code = 412
            return HttpResponse(status_code)

# 地质数据删除数据


def DeleteGeologicalInfo(request):
    """
    docstring
    """
    if request.method == "POST":
        body_data = request.body
        # print(body_data)
        data_json = json.loads(body_data)
        # print(data_json)
        query_data_json = data_json['json_data']
        # print(query_data_json)
        dict_data = json.loads(query_data_json)
        print(dict_data)
        front_query_oid = dict_data['id']

        query_obj = GeologicalInfo.objects.get(
            id=front_query_oid)
        print(query_obj)
        query_obj.delete()
        return HttpResponse("Delete Success")

# 地质数据查询数据


class GeologicalInfoSearch(APIView):
    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        # print('success')
        search_key = request.GET['search_key']  # 根据字段搜索
        # print(search_key)
        geological_obj = GeologicalInfo.objects.filter(
            geological_filename=search_key).all().order_by('_id')  # 一定要排序
        # seismic_obj = SeismicInfo.objects.search_text(search_key).first()

        # 创建分页对象
        page = MyPagination()
        # 实例化查询，获取分页的数据
        page_chapter = page.paginate_queryset(
            queryset=geological_obj, request=request, view=self)
        # 序列化及结果返回，将分页后返回的数据, 进行序列化
        ser = GeologicalInfoSerializer(instance=page_chapter, many=True)
        data = {'list': ser.data}
        return page.get_paginated_response(data)


# 地质数据下载数据
@require_http_methods(['GET'])
def GeologicalFileDownload(request):

    search_key = request.GET['file_id']  # 根据字段搜索
    print(search_key)

    # 从数据库拿到数据
    geological_obj = GeologicalInfo.objects(id=search_key).first()
    print(geological_obj)
    print(geological_obj.geological_filename)
    filename = geological_obj.geological_filename
    geological_file = geological_obj.filedata.read()
    content_type = geological_obj.filedata.content_type
    # print(type(seismic_file)) #<class 'bytes'>
    # print(type(content_type)) #<class 'str'>

    # 数据写入服务器
    with open("../mongeostore_env/upload/%s" % filename, 'wb') as f:
        f.write(geological_file)
    print('save success')

    # # 拿到数据,返回前端
    with open("./upload/%s" % filename, "rb") as f:
        res = HttpResponse(f)
        res["Content-Type"] = "application/octet-stream"  # 注意格式
        res["Content-Disposition"] = 'filename="{}"'.format(filename)
    return res
    # return HttpResponse('success')
# 水文数据上传


class HydrologicalInfoView(APIView):
    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        hydrological_obj = HydrologicalInfo.objects.all().order_by('_id')  # 一定要排序
        # print(seismic_obj)
        # 创建分页对象
        page = MyPagination()
        # 实例化查询，获取分页的数据
        page_chapter = page.paginate_queryset(
            queryset=hydrological_obj, request=request, view=self)
        # 序列化及结果返回，将分页后返回的数据, 进行序列化
        ser = HydrologicalInfoSerializer(instance=page_chapter, many=True)
        data = {'list': ser.data}
        return page.get_paginated_response(data)

    def post(self, request, *args, **kwargs):
        """
        docstring
        """
        fileio = request.FILES.get("file", None)  # 注意比较

        # print(request.data['upload_date'])  # DRF才有request.data
        # print(request.POST)  # Django只有request.POST、request.GET
        # print(request.data)
        # _id = self.request.POST.get('id')
        # 取出来竟是个元组，QAQ
        hydrological_filename = request.data['hydrological_filename'],
        location = request.data['location'],
        company_name = request.data['company_name'],
        uploader = request.data['uploader'],
        project_name = request.data['project_name'],
        hydrological_upload_date = request.data['hydrological_upload_date'],
        # 上传到GriDFS中
        filename = request.data['filename'],

        temp_time2 = int(hydrological_upload_date[0])/1000
        # 转换成localtime
        time_local2 = time.localtime(temp_time2)
        # 转换成新的时间格式(2016-05-05 20:28:54)

        dt2 = time.strftime("%Y-%m-%d", time_local2)

        # 保存到本地
        if not os.path.exists('upload/'):
            os.mkdir('upload/')
        with open("./upload/%s" % fileio.name, 'wb+') as f:
            for chunk in fileio.chunks():
                f.write(chunk)
            f.close()
        # 写入数据
        write_data = HydrologicalInfo(
            hydrological_filename=hydrological_filename[0],
            location=location[0],
            project_name=project_name[0], company_name=company_name[0], uploader=uploader[0],
            hydrological_upload_date=dt2)

        with open("./upload/%s" % fileio.name, 'rb') as fd:
            # 写入GridFS
            write_data.filedata.put(
                fd, content_type='jpeg/png', filename=hydrological_filename[0], aliases=[filename[0]])
            # writedata.filedata.put(SeismicInfo, content_type='segy')
        write_data.save()

        return HttpResponse('success')


# 水文数据编辑数据
def EditHydrologicalInfo(request):
    if request.method == "POST":

        body_data = request.body
        data_json = json.loads(body_data)
        # print(data_json)

        query_data_json = data_json['json_data']
        dict_data = json.loads(query_data_json)
        dict_data.pop('filedata')  # 去掉文件字段
        front_query_oid = dict_data['id']

        query_obj = HydrologicalInfo.objects.get(
            id=front_query_oid)
        print(query_obj)
        try:
            query_obj.update(**dict_data)
            query_obj.save()
            return HttpResponse('success')
        except:
            print('输入有误')
            status_code = 412
            return HttpResponse(status_code)

# 水文数据删除数据


def DeleteHydrologicalInfo(request):
    """
    docstring
    """
    if request.method == "POST":
        body_data = request.body
        # print(body_data)
        data_json = json.loads(body_data)
        # print(data_json)
        query_data_json = data_json['json_data']
        # print(query_data_json)
        dict_data = json.loads(query_data_json)
        print(dict_data)
        front_query_oid = dict_data['id']

        query_obj = HydrologicalInfo.objects.get(
            id=front_query_oid)
        print(query_obj)
        query_obj.delete()
        return HttpResponse("Delete Success")

# 水文数据查询数据


class HydrologicalInfoSearch(APIView):
    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        # print('success')
        search_key = request.GET['search_key']  # 根据字段搜索
        # print(search_key)
        hydrological_obj = HydrologicalInfo.objects.filter(
            hydrological_filename=search_key).all().order_by('_id')  # 一定要排序
        # seismic_obj = SeismicInfo.objects.search_text(search_key).first()

        # 创建分页对象
        page = MyPagination()
        # 实例化查询，获取分页的数据
        page_chapter = page.paginate_queryset(
            queryset=hydrological_obj, request=request, view=self)
        # 序列化及结果返回，将分页后返回的数据, 进行序列化
        ser = HydrologicalInfoSerializer(instance=page_chapter, many=True)
        data = {'list': ser.data}
        return page.get_paginated_response(data)


# 水文数据下载数据
@require_http_methods(['GET'])
def HydrologicalFileDownload(request):

    search_key = request.GET['file_id']  # 根据字段搜索
    print(search_key)

    # 从数据库拿到数据
    hydrological_obj = HydrologicalInfo.objects(id=search_key).first()
    print(hydrological_obj)
    print(hydrological_obj.hydrological_filename)
    filename = hydrological_obj.hydrological_filename
    hydrological_file = hydrological_obj.filedata.read()
    content_type = hydrological_obj.filedata.content_type
    # print(type(seismic_file)) #<class 'bytes'>
    # print(type(content_type)) #<class 'str'>

    # 数据写入服务器
    with open("../mongeostore_env/upload/%s" % filename, 'wb') as f:
        f.write(hydrological_file)
    print('save success')

    # # 拿到数据,返回前端
    with open("./upload/%s" % filename, "rb") as f:
        res = HttpResponse(f)
        res["Content-Type"] = "application/octet-stream"  # 注意格式
        res["Content-Disposition"] = 'filename="{}"'.format(filename)
    return res
    # return HttpResponse('success')


#########地震采集数据上传##########
class SeiAcquisitionInfoView(APIView):
    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        seiAcquisition_obj = SeiAcquisitionInfo.objects.all().order_by('_id')  # 一定要排序
        # print(seismic_obj)
        # 创建分页对象
        page = MyPagination()
        # 实例化查询，获取分页的数据
        page_chapter = page.paginate_queryset(
            queryset=seiAcquisition_obj, request=request, view=self)
        # 序列化及结果返回，将分页后返回的数据, 进行序列化
        ser = SeiAcquisitionInfoSerializer(instance=page_chapter, many=True)
        data = {'list': ser.data}
        return page.get_paginated_response(data)

    def post(self, request, *args, **kwargs):
        """
        docstring
        """
        fileio = request.FILES.get("file", None)  # 注意比较

        # print(request.data['upload_date'])  # DRF才有request.data
        # print(request.POST)  # Django只有request.POST、request.GET
        # print(request.data)
        # _id = self.request.POST.get('id')
        seiAcquisition_filename = request.data['seiAcquisition_filename'],  # 取出来竟是个元组，QAQ
        location = request.data['location'],
        company_name = request.data['company_name'],
        uploader = request.data['uploader'],
        project_name = request.data['project_name'],
        seiAcquisition_upload_date = request.data['seiAcquisition_upload_date'],
        # 上传到GriDFS中
        filename = request.data['filename'],

        temp_time2 = int(seiAcquisition_upload_date[0])/1000
        # 转换成localtime
        time_local2 = time.localtime(temp_time2)
        # 转换成新的时间格式(2016-05-05 20:28:54)

        dt2 = time.strftime("%Y-%m-%d", time_local2)

        # 保存到本地
        if not os.path.exists('upload/'):
            os.mkdir('upload/')
        with open("./upload/%s" % fileio.name, 'wb+') as f:
            for chunk in fileio.chunks():
                f.write(chunk)
            f.close()
        # 写入数据
        write_data = SeiAcquisitionInfo(
            seiAcquisition_filename=seiAcquisition_filename[0],
            location=location[0],
            project_name=project_name[0], company_name=company_name[0], uploader=uploader[0],
            seiAcquisition_upload_date=dt2)

        with open("./upload/%s" % fileio.name, 'rb') as fd:
            # 写入GridFS
            write_data.filedata.put(
                fd, content_type='jpeg/png', filename=seiAcquisition_filename[0], aliases=[filename[0]])
            # writedata.filedata.put(SeismicInfo, content_type='segy')
        write_data.save()

        return HttpResponse('success')


# 地震采集数据编辑数据
def EditSeiAcquisitionInfo(request):
    if request.method == "POST":

        body_data = request.body
        data_json = json.loads(body_data)
        # print(data_json)

        query_data_json = data_json['json_data']
        dict_data = json.loads(query_data_json)
        dict_data.pop('filedata')  # 去掉文件字段
        front_query_oid = dict_data['id']

        query_obj = SeiAcquisitionInfo.objects.get(
            id=front_query_oid)
        print(query_obj)
        try:
            query_obj.update(**dict_data)
            query_obj.save()
            return HttpResponse('success')
        except:
            print('输入有误')
            status_code = 412
            return HttpResponse(status_code)
        
# 地震采集数据删除数据
def DeleteSeiAcquisitionInfo(request):
    """
    docstring
    """
    if request.method == "POST":
        body_data = request.body
        # print(body_data)
        data_json = json.loads(body_data)
        # print(data_json)
        query_data_json = data_json['json_data']
        # print(query_data_json)
        dict_data = json.loads(query_data_json)
        print(dict_data)
        front_query_oid = dict_data['id']

        query_obj = SeiAcquisitionInfo.objects.get(
            id=front_query_oid)
        print(query_obj)
        query_obj.delete()
        return HttpResponse("Delete Success")

# 地震采集数据查询数据
class SeiAcquisitionInfoSearch(APIView):
    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        # print('success')
        search_key = request.GET['search_key']  # 根据字段搜索
        # print(search_key)
        seiAcquisition_obj = SeiAcquisitionInfo.objects.filter(
            seiAcquisition_filename=search_key).all().order_by('_id')  # 一定要排序
        # seismic_obj = SeismicInfo.objects.search_text(search_key).first()

        # 创建分页对象
        page = MyPagination()
        # 实例化查询，获取分页的数据
        page_chapter = page.paginate_queryset(
            queryset=seiAcquisition_obj, request=request, view=self)
        # 序列化及结果返回，将分页后返回的数据, 进行序列化
        ser = SeiAcquisitionInfoSerializer(instance=page_chapter, many=True)
        data = {'list': ser.data}
        return page.get_paginated_response(data)


# 地震采集数据下载数据
@require_http_methods(['GET'])
def SeiAcquisitionFileDownload(request):

    search_key = request.GET['file_id']  # 根据字段搜索
    print(search_key)

    # 从数据库拿到数据
    seiAcquisition_obj = SeiAcquisitionInfo.objects(id=search_key).first()
    print(seiAcquisition_obj)
    print(seiAcquisition_obj.seiAcquisition_filename)
    filename = seiAcquisition_obj.seiAcquisition_filename
    seiAcquisition_file = seiAcquisition_obj.filedata.read()
    content_type = seiAcquisition_obj.filedata.content_type
    # print(type(seismic_file)) #<class 'bytes'>
    # print(type(content_type)) #<class 'str'>

    # 数据写入服务器
    with open("../mongeostore_env/upload/%s" % filename, 'wb') as f:
        f.write(seiAcquisition_file)
    print('save success')

    # # 拿到数据,返回前端
    with open("./upload/%s" % filename, "rb") as f:
        res = HttpResponse(f)
        res["Content-Type"] = "application/octet-stream"  # 注意格式
        res["Content-Disposition"] = 'filename="{}"'.format(filename)
    return res
    # return HttpResponse('success')



#########地震处理数据上传##########
class SeiprocessInfoView(APIView):
    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        seiprocess_obj = SeiprocessInfo.objects.all().order_by('_id')  # 一定要排序
        # print(seismic_obj)
        # 创建分页对象
        page = MyPagination()
        # 实例化查询，获取分页的数据
        page_chapter = page.paginate_queryset(
            queryset=seiprocess_obj, request=request, view=self)
        # 序列化及结果返回，将分页后返回的数据, 进行序列化
        ser = SeiprocessInfoSerializer(instance=page_chapter, many=True)
        data = {'list': ser.data}
        return page.get_paginated_response(data)

    def post(self, request, *args, **kwargs):
        """
        docstring
        """
        fileio = request.FILES.get("file", None)  # 注意比较

        # print(request.data['upload_date'])  # DRF才有request.data
        # print(request.POST)  # Django只有request.POST、request.GET
        # print(request.data)
        # _id = self.request.POST.get('id')
        seiprocess_filename = request.data['seiprocess_filename'],  # 取出来竟是个元组，QAQ
        location = request.data['location'],
        company_name = request.data['company_name'],
        uploader = request.data['uploader'],
        project_name = request.data['project_name'],
        seiprocess_upload_date = request.data['seiprocess_upload_date'],
        # 上传到GriDFS中
        filename = request.data['filename'],

        temp_time2 = int(seiprocess_upload_date[0])/1000
        # 转换成localtime
        time_local2 = time.localtime(temp_time2)
        # 转换成新的时间格式(2016-05-05 20:28:54)

        dt2 = time.strftime("%Y-%m-%d", time_local2)

        # 保存到本地
        if not os.path.exists('upload/'):
            os.mkdir('upload/')
        with open("./upload/%s" % fileio.name, 'wb+') as f:
            for chunk in fileio.chunks():
                f.write(chunk)
            f.close()
        # 写入数据
        write_data = SeiprocessInfo(
            seiprocess_filename=seiprocess_filename[0],
            location=location[0],
            project_name=project_name[0], company_name=company_name[0], uploader=uploader[0],
            seiprocess_upload_date=dt2)

        with open("./upload/%s" % fileio.name, 'rb') as fd:
            # 写入GridFS
            write_data.filedata.put(
                fd, content_type='jpeg/png', filename=seiprocess_filename[0], aliases=[filename[0]])
            # writedata.filedata.put(SeismicInfo, content_type='segy')
        write_data.save()

        return HttpResponse('success')


# 地震处理数据编辑数据
def EditSeiprocessInfo(request):
    if request.method == "POST":

        body_data = request.body
        data_json = json.loads(body_data)
        # print(data_json)

        query_data_json = data_json['json_data']
        dict_data = json.loads(query_data_json)
        dict_data.pop('filedata')  # 去掉文件字段
        front_query_oid = dict_data['id']

        query_obj = SeiprocessInfo.objects.get(
            id=front_query_oid)
        print(query_obj)
        try:
            query_obj.update(**dict_data)
            query_obj.save()
            return HttpResponse('success')
        except:
            print('输入有误')
            status_code = 412
            return HttpResponse(status_code)
        
# 地震处理数据删除数据
def DeleteSeiprocessInfo(request):
    """
    docstring
    """
    if request.method == "POST":
        body_data = request.body
        # print(body_data)
        data_json = json.loads(body_data)
        # print(data_json)
        query_data_json = data_json['json_data']
        # print(query_data_json)
        dict_data = json.loads(query_data_json)
        print(dict_data)
        front_query_oid = dict_data['id']

        query_obj = SeiprocessInfo.objects.get(
            id=front_query_oid)
        print(query_obj)
        query_obj.delete()
        return HttpResponse("Delete Success")

# 地震处理数据查询数据
class SeiprocessInfoSearch(APIView):
    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        # print('success')
        search_key = request.GET['search_key']  # 根据字段搜索
        # print(search_key)
        seiprocess_obj = SeiprocessInfo.objects.filter(
            seiprocess_filename=search_key).all().order_by('_id')  # 一定要排序
        # seismic_obj = SeismicInfo.objects.search_text(search_key).first()

        # 创建分页对象
        page = MyPagination()
        # 实例化查询，获取分页的数据
        page_chapter = page.paginate_queryset(
            queryset=seiprocess_obj, request=request, view=self)
        # 序列化及结果返回，将分页后返回的数据, 进行序列化
        ser = SeiprocessInfoSerializer(instance=page_chapter, many=True)
        data = {'list': ser.data}
        return page.get_paginated_response(data)


# 地震处理数据下载数据
@require_http_methods(['GET'])
def SeiprocessFileDownload(request):

    search_key = request.GET['file_id']  # 根据字段搜索
    print(search_key)

    # 从数据库拿到数据
    seiprocess_obj = SeiprocessInfo.objects(id=search_key).first()
    print(seiprocess_obj)
    print(seiprocess_obj.seiprocess_filename)
    filename = seiprocess_obj.seiprocess_filename
    seiprocess_file = seiprocess_obj.filedata.read()
    content_type = seiprocess_obj.filedata.content_type
    # print(type(seismic_file)) #<class 'bytes'>
    # print(type(content_type)) #<class 'str'>

    # 数据写入服务器
    with open("../mongeostore_env/upload/%s" % filename, 'wb') as f:
        f.write(seiprocess_file)
    print('save success')

    # # 拿到数据,返回前端
    with open("./upload/%s" % filename, "rb") as f:
        res = HttpResponse(f)
        res["Content-Type"] = "application/octet-stream"  # 注意格式
        res["Content-Disposition"] = 'filename="{}"'.format(filename)
    return res
    # return HttpResponse('success')



#########地震解释数据上传##########
class SeiInterpretationInfoView(APIView):
    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        seiInterpretation_obj = SeiInterpretationInfo.objects.all().order_by('_id')  # 一定要排序
        # print(seismic_obj)
        # 创建分页对象
        page = MyPagination()
        # 实例化查询，获取分页的数据
        page_chapter = page.paginate_queryset(
            queryset=seiInterpretation_obj, request=request, view=self)
        # 序列化及结果返回，将分页后返回的数据, 进行序列化
        ser = SeiInterpretationInfoSerializer(instance=page_chapter, many=True)
        data = {'list': ser.data}
        return page.get_paginated_response(data)

    def post(self, request, *args, **kwargs):
        """
        docstring
        """
        fileio = request.FILES.get("file", None)  # 注意比较

        # print(request.data['upload_date'])  # DRF才有request.data
        # print(request.POST)  # Django只有request.POST、request.GET
        # print(request.data)
        # _id = self.request.POST.get('id')
        seiInterpretation_filename = request.data['seiInterpretation_filename'],  # 取出来竟是个元组，QAQ
        location = request.data['location'],
        company_name = request.data['company_name'],
        uploader = request.data['uploader'],
        project_name = request.data['project_name'],
        seiInterpretation_upload_date = request.data['seiInterpretation_upload_date'],
        # 上传到GriDFS中
        filename = request.data['filename'],

        temp_time2 = int(seiInterpretation_upload_date[0])/1000
        # 转换成localtime
        time_local2 = time.localtime(temp_time2)
        # 转换成新的时间格式(2016-05-05 20:28:54)

        dt2 = time.strftime("%Y-%m-%d", time_local2)

        # 保存到本地
        if not os.path.exists('upload/'):
            os.mkdir('upload/')
        with open("./upload/%s" % fileio.name, 'wb+') as f:
            for chunk in fileio.chunks():
                f.write(chunk)
            f.close()
        # 写入数据
        write_data = SeiInterpretationInfo(
            seiInterpretation_filename=seiInterpretation_filename[0],
            location=location[0],
            project_name=project_name[0], company_name=company_name[0], uploader=uploader[0],
            seiInterpretation_upload_date=dt2)

        with open("./upload/%s" % fileio.name, 'rb') as fd:
            # 写入GridFS
            write_data.filedata.put(
                fd, content_type='jpeg/png', filename=seiInterpretation_filename[0], aliases=[filename[0]])
            # writedata.filedata.put(SeismicInfo, content_type='segy')
        write_data.save()

        return HttpResponse('success')


# 地震解释数据编辑数据
def EditSeiInterpretationInfo(request):
    if request.method == "POST":

        body_data = request.body
        data_json = json.loads(body_data)
        # print(data_json)

        query_data_json = data_json['json_data']
        dict_data = json.loads(query_data_json)
        dict_data.pop('filedata')  # 去掉文件字段
        front_query_oid = dict_data['id']

        query_obj = SeiInterpretationInfo.objects.get(
            id=front_query_oid)
        print(query_obj)
        try:
            query_obj.update(**dict_data)
            query_obj.save()
            return HttpResponse('success')
        except:
            print('输入有误')
            status_code = 412
            return HttpResponse(status_code)
        
# 地震解释数据删除数据
def DeleteSeiInterpretationInfo(request):
    """
    docstring
    """
    if request.method == "POST":
        body_data = request.body
        # print(body_data)
        data_json = json.loads(body_data)
        # print(data_json)
        query_data_json = data_json['json_data']
        # print(query_data_json)
        dict_data = json.loads(query_data_json)
        print(dict_data)
        front_query_oid = dict_data['id']

        query_obj = SeiInterpretationInfo.objects.get(
            id=front_query_oid)
        print(query_obj)
        query_obj.delete()
        return HttpResponse("Delete Success")

# 地震解释数据查询数据
class SeiInterpretationInfoSearch(APIView):
    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        # print('success')
        search_key = request.GET['search_key']  # 根据字段搜索
        # print(search_key)
        seiInterpretation_obj = SeiInterpretationInfo.objects.filter(
            seiInterpretation_filename=search_key).all().order_by('_id')  # 一定要排序
        # seismic_obj = SeismicInfo.objects.search_text(search_key).first()

        # 创建分页对象
        page = MyPagination()
        # 实例化查询，获取分页的数据
        page_chapter = page.paginate_queryset(
            queryset=seiInterpretation_obj, request=request, view=self)
        # 序列化及结果返回，将分页后返回的数据, 进行序列化
        ser = SeiInterpretationInfoSerializer(instance=page_chapter, many=True)
        data = {'list': ser.data}
        return page.get_paginated_response(data)


# 地震历使数据下载数据
@require_http_methods(['GET'])
def SeiInterpretationFileDownload(request):

    search_key = request.GET['file_id']  # 根据字段搜索
    print(search_key)

    # 从数据库拿到数据
    seiInterpretation_obj = SeiInterpretationInfo.objects(id=search_key).first()
    print(seiInterpretation_obj)
    print(seiInterpretation_obj.seiInterpretation_filename)
    filename = seiInterpretation_obj.seiInterpretation_filename
    seiInterpretation_file = seiInterpretation_obj.filedata.read()
    content_type = seiInterpretation_obj.filedata.content_type
    # print(type(seismic_file)) #<class 'bytes'>
    # print(type(content_type)) #<class 'str'>

    # 数据写入服务器
    with open("../mongeostore_env/upload/%s" % filename, 'wb') as f:
        f.write(seiInterpretation_file)
    print('save success')

    # # 拿到数据,返回前端
    with open("./upload/%s" % filename, "rb") as f:
        res = HttpResponse(f)
        res["Content-Type"] = "application/octet-stream"  # 注意格式
        res["Content-Disposition"] = 'filename="{}"'.format(filename)
    return res
    # return HttpResponse('success')


#########地震历史数据上传##########
class SeihistoricalInfoView(APIView):
    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        seihistorical_obj = SeihistoricalInfo.objects.all().order_by('_id')  # 一定要排序
        # print(seismic_obj)
        # 创建分页对象
        page = MyPagination()
        # 实例化查询，获取分页的数据
        page_chapter = page.paginate_queryset(
            queryset=seihistorical_obj, request=request, view=self)
        # 序列化及结果返回，将分页后返回的数据, 进行序列化
        ser = SeihistoricalInfoSerializer(instance=page_chapter, many=True)
        data = {'list': ser.data}
        return page.get_paginated_response(data)

    def post(self, request, *args, **kwargs):
        """
        docstring
        """
        fileio = request.FILES.get("file", None)  # 注意比较

        # print(request.data['upload_date'])  # DRF才有request.data
        # print(request.POST)  # Django只有request.POST、request.GET
        # print(request.data)
        # _id = self.request.POST.get('id')
        seihistorical_filename = request.data['seihistorical_filename'],  # 取出来竟是个元组，QAQ
        location = request.data['location'],
        company_name = request.data['company_name'],
        uploader = request.data['uploader'],
        project_name = request.data['project_name'],
        seihistorical_upload_date = request.data['seihistorical_upload_date'],
        # 上传到GriDFS中
        filename = request.data['filename'],

        temp_time2 = int(seihistorical_upload_date[0])/1000
        # 转换成localtime
        time_local2 = time.localtime(temp_time2)
        # 转换成新的时间格式(2016-05-05 20:28:54)

        dt2 = time.strftime("%Y-%m-%d", time_local2)

        # 保存到本地
        if not os.path.exists('upload/'):
            os.mkdir('upload/')
        with open("./upload/%s" % fileio.name, 'wb+') as f:
            for chunk in fileio.chunks():
                f.write(chunk)
            f.close()
        # 写入数据
        write_data = SeihistoricalInfo(
            seihistorical_filename=seihistorical_filename[0],
            location=location[0],
            project_name=project_name[0], company_name=company_name[0], uploader=uploader[0],
            seihistorical_upload_date=dt2)

        with open("./upload/%s" % fileio.name, 'rb') as fd:
            # 写入GridFS
            write_data.filedata.put(
                fd, content_type='jpeg/png', filename=seihistorical_filename[0], aliases=[filename[0]])
            # writedata.filedata.put(SeismicInfo, content_type='segy')
        write_data.save()

        return HttpResponse('success')


# 地震历史数据编辑数据
def EditSeihistoricalInfo(request):
    if request.method == "POST":

        body_data = request.body
        data_json = json.loads(body_data)
        # print(data_json)

        query_data_json = data_json['json_data']
        dict_data = json.loads(query_data_json)
        dict_data.pop('filedata')  # 去掉文件字段
        front_query_oid = dict_data['id']

        query_obj = SeihistoricalInfo.objects.get(
            id=front_query_oid)
        print(query_obj)
        try:
            query_obj.update(**dict_data)
            query_obj.save()
            return HttpResponse('success')
        except:
            print('输入有误')
            status_code = 412
            return HttpResponse(status_code)
        
# 地震历史数据删除数据
def DeleteSeihistoricalInfo(request):
    """
    docstring
    """
    if request.method == "POST":
        body_data = request.body
        # print(body_data)
        data_json = json.loads(body_data)
        # print(data_json)
        query_data_json = data_json['json_data']
        # print(query_data_json)
        dict_data = json.loads(query_data_json)
        print(dict_data)
        front_query_oid = dict_data['id']

        query_obj = SeihistoricalInfo.objects.get(
            id=front_query_oid)
        print(query_obj)
        query_obj.delete()
        return HttpResponse("Delete Success")

# 地震历史数据查询数据
class SeihistoricalInfoSearch(APIView):
    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        # print('success')
        search_key = request.GET['search_key']  # 根据字段搜索
        # print(search_key)
        seihistorical_obj = SeihistoricalInfo.objects.filter(
            seihistorical_filename=search_key).all().order_by('_id')  # 一定要排序
        # seismic_obj = SeismicInfo.objects.search_text(search_key).first()

        # 创建分页对象
        page = MyPagination()
        # 实例化查询，获取分页的数据
        page_chapter = page.paginate_queryset(
            queryset=seihistorical_obj, request=request, view=self)
        # 序列化及结果返回，将分页后返回的数据, 进行序列化
        ser = SeihistoricalInfoSerializer(instance=page_chapter, many=True)
        data = {'list': ser.data}
        return page.get_paginated_response(data)


# 地震历史数据下载数据
@require_http_methods(['GET'])
def SeihistoricalFileDownload(request):

    search_key = request.GET['file_id']  # 根据字段搜索
    print(search_key)

    # 从数据库拿到数据
    seihistorical_obj = SeihistoricalInfo.objects(id=search_key).first()
    print(seihistorical_obj)
    print(seihistorical_obj.seihistorical_filename)
    filename = seihistorical_obj.seihistorical_filename
    seihistorical_file = seihistorical_obj.filedata.read()
    content_type = seihistorical_obj.filedata.content_type
    # print(type(seismic_file)) #<class 'bytes'>
    # print(type(content_type)) #<class 'str'>

    # 数据写入服务器
    with open("../mongeostore_env/upload/%s" % filename, 'wb') as f:
        f.write(seihistorical_file)
    print('save success')

    # # 拿到数据,返回前端
    with open("./upload/%s" % filename, "rb") as f:
        res = HttpResponse(f)
        res["Content-Type"] = "application/octet-stream"  # 注意格式
        res["Content-Disposition"] = 'filename="{}"'.format(filename)
    return res
    # return HttpResponse('success')
