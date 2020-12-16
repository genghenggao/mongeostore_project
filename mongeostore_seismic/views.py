'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-12-16 21:36:57
LastEditors: henggao
LastEditTime: 2020-12-16 23:15:33
'''
import time
from django.http.response import HttpResponse
from mongoengine.context_managers import switch_collection
from rest_framework.views import APIView
from .models import SeismicInfo
# Create your views here.


class SeismicInfoView(APIView):
    def get(request):
        """
        docstring
        """
        pass

    def post(self, request):
        """
        docstring
        """
        zk_histogram = request.FILES.get("file", None)  # 注意比较

        print(request.data['upload_date'])  # DRF才有request.data
        print(request.POST)  # Django只有request.POST、request.GET
        _id = self.request.POST.get('id')
        filename = request.data['filename'],  # 取出来竟是个元组，QAQ
        location = request.data['location'],
        company_name = request.data['company_name'],
        uploader = request.data['uploader'],
        project_name = request.data['project_name'],
        upload_date = request.data['uploaddate'],  # 这个字段前端会冲突，另起

        temp_time2 = int(upload_date[0])/1000
        # 转换成localtime
        time_local2 = time.localtime(temp_time2)
        # 转换成新的时间格式(2016-05-05 20:28:54)
        # dt1 = time.strftime("%Y-%m-%d %H:%M:%S", time_local1)
        # dt2 = time.strftime("%Y-%m-%d %H:%M:%S", time_local2)
        dt2 = time.strftime("%Y-%m-%d", time_local2)
        # test = DrillMetaModel(zk_num='ZK1')
        # test.save() # update时,使用save方法
        # # DrillMetaModel.objects.create(zk_num="ZK1")
        with switch_collection(SeismicInfo, '地震数据Demo2') as SeismicInfo:
            report_form = SeismicInfo(title=request.POST.get('filename'))
            writedata = SeismicInfo(_id=_id,
                                    filename=filename[0],
                                    location=location[0],
                                    project_name=project_name[0], company_name=company_name[0], uploader=uploader[0],
                                    upload_date=dt2)
            # writedata.filedata.put(SeismicInfo,content_type='')
            writedata.filedata.put(SeismicInfo, content_type='')
            writedata.save()

        return HttpResponse('success')
