'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-23 21:47:34
LastEditors: henggao
LastEditTime: 2020-10-26 22:28:22
'''
from django.http import response
from .models import FileInfo, FileInfo2
from rest_framework.views import APIView
from .serializers import FileInfo2Serializer, FileInfoSerializer
from typing import ClassVar
from django.http import HttpResponse
from django.shortcuts import render
from pymongo import mongo_client
import json

# Create your views here.


def uploadfile(request, *args, **kwargs):
    """
    docstring
    """
    print("Hello Uploader")
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
        print("经过这里")
        print(myFile)
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


class FileInfoView(APIView):

    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        print("走的时GET方法")
        response = {}
        queryset = FileInfo.objects.all()
        serializer_class = FileInfoSerializer
        response['code'] = 200
        # response["Access-Control-Allow-Methods"] = "POST"
        return HttpResponse(json.dumps(response), content_type="application/json")

    def post(self, request, *args, **kwargs):
        """
        docstring
        """
        print("走的时POST方法")
        file_id = self.request.POST.get('id')
        filename = self.request.POST.get('name')
        publiser = self.request.POST.get('publisher')
        print(file_id)
        print(filename)
        data = {

        }
        return HttpResponse("post success")


class FileInfo2View(APIView):

    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        print("走的时GET方法")
        response = {}
        queryset = FileInfo2.objects.all()
        serializer_class = FileInfo2Serializer
        response['code'] = 200
        # response["Access-Control-Allow-Methods"] = "POST"
        return HttpResponse(json.dumps(response), content_type="application/json")

    def post(self, request, *args, **kwargs):
        """
        docstring
        """
        print("走的时POST方法")
        filename = self.request.POST.get('filename')

        print(filename)
        return HttpResponse("post success")