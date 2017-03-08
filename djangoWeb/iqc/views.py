from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import IQCDataCVTE6486COPY, IQCUploadRecord
from django.db.utils import IntegrityError
from django.core import serializers
import json


# Create your views here.
# 上传数据
# @login_required(login_url='/?message=login')
@login_required(login_url='/login/')
@permission_required('iqc.upload_IQCDataCVTE6486COPY', login_url='/?message=permission')
def upload_data(request):
    if request.method == 'POST':
        excel_data = request.POST.get('exceldata')
        excel_data_dict = json.loads(excel_data)  # 数据类型格式为dict
        result = {'success': False,
                  'message': ''
                  }

        for data in excel_data_dict:
            print(data["条码"])
            if data["生成批次"] != "生成批次":
                try:
                    if IQCDataCVTE6486COPY.objects.filter(tm=data["条码"]).exists():
                        result['message'] = "'" + data["条码"] + "'在数据库中已经存在"
                        return HttpResponse(json.dumps(result))
                except Exception as e:
                    result['message'] = e
                    return HttpResponse(json.dumps(result))
        for data in excel_data_dict:
            if data["生成批次"] != "生成批次" :
                try:
                    insert_excel_data = IQCDataCVTE6486COPY(scpc=data["生成批次"], tm=data["条码"], gwmc=data["工位名称"],
                                        pzxxbh=data["品质现象编号"], pzxxmc=data["品质现象名称"],
                                        cssj=data["测试时间"].replace('/','-'))
                    insert_excel_data.save(force_insert=True)
                except IntegrityError as e:
                    result['message'] = "'" + data["条码"] + "'在数据库中已经存在"
                    return HttpResponse(json.dumps(result))
                except Exception as e:
                    result['message'] = e
                    return HttpResponse(json.dumps(result))
        upload_record_data = IQCUploadRecord(person=request.user, upload_num=len(excel_data_dict)-1)
        upload_record_data.save(force_insert=True)
        result['success'] = True
        result['message'] = "ok"
        return HttpResponse(json.dumps(result))
    else:
        return render(request,'iqc/iqc-upload-data.html')


# 查询数据
@login_required(login_url='/login/')
def search_data(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'iqc/iqc-search-data.html')
        # result_timeline = IQCUploadRecord.objects.all()
        # for item in result_timeline:
        #     print(item.person.first_name)
        #     print(item.upload_num)
        # return render(request, 'iqc/iqc-search-data.html', {'result_timeline': result_timeline})


# 时间轴
@login_required
def iqc_timeline(request):
    if request.method == 'GET':
        result_timeline = IQCUploadRecord.objects.all()
        return render(request, 'iqc/timeline.html', {'result_timeline': result_timeline})
