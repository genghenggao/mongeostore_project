'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-12-16 21:36:57
LastEditors: henggao
LastEditTime: 2020-12-17 22:20:34
'''
import json
from django import http
from django.views.decorators.http import require_http_methods

from rest_framework import filters
from .serializers import SeismicInfoSerializer
import os
from rest_framework.response import Response

from rest_framework.pagination import PageNumberPagination
from .models import SeismicInfo
import time
from django.http.response import HttpResponse
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
        print(seismic_obj)
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

        print(request.data['upload_date'])  # DRF才有request.data
        print(request.POST)  # Django只有request.POST、request.GET
        print(request.data)
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
        print('success')
        search_key = request.GET['search_key']  # 根据字段搜索
        print(search_key)
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