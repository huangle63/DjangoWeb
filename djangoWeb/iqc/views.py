from django.shortcuts import render, HttpResponse
from .models import IQCDataCVTE6486COPY
from django.db.utils import IntegrityError
import json
import copy


# Create your views here.
# 上传数据
def upload_data(request):
    if request.method == 'POST':
        excel_data = request.POST.get('exceldata')
        excel_data_dict = json.loads(excel_data)  # 数据类型格式为dict
        result = {'success': False,
                  'message': ''
                  }

        for data in excel_data_dict:
            print(data["条码"])
            if(data["生成批次"] != "生成批次"):
                try:
                    if IQCDataCVTE6486COPY.objects.filter(tm=data["条码"]).exists():
                        result['message'] = "'" + data["条码"] + "'在数据库中已经存在"
                        return HttpResponse(json.dumps(result))
                except Exception as e:
                    result['message'] = e
                    return HttpResponse(json.dumps(result))
        for data in excel_data_dict:
            if(data["生成批次"] != "生成批次"):
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
        result['success'] = True
        result['message'] = "ok"
        return HttpResponse(json.dumps(result))
    else:
        return render(request,'iqc/iqc-upload-data.html')


# 查询数据
def search_data(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'iqc/iqc-search-data.html')
