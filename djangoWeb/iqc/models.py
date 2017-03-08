from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


# Create your models here.


class IQCDataCVTE6486COPY(models.Model):
    scpc = models.CharField(max_length=100, verbose_name="生成批次")  #
    tm = models.CharField(max_length=100,unique=True, verbose_name="条码")  #
    gwmc = models.CharField(max_length=100, verbose_name="工位名称")  #
    pzxxbh = models.CharField(max_length=100, verbose_name="品质现象编号")  #
    pzxxmc = models.CharField(max_length=100, verbose_name="品质现象名称")  #
    cssj = models.DateTimeField(verbose_name="测试时间")  #
    # csly = models.CharField(max_length=100)  #
    # cswz = models.CharField(max_length=100)  #
    # csr = models.CharField(max_length=100)  #
    # mj = models.CharField(max_length=100)  #
    # csxtbh = models.CharField(max_length=100)  #
    # csly = models.CharField(max_length=100)  #
    # csly = models.CharField(max_length=100)  #
    # csly = models.CharField(max_length=100)  #

    # python2使用__unicode__, python3使用__str__
    def __str__(self):
        return self.tm

    class Meta:
        permissions =(
            ("search_IQCDataCVTE6486COPY","can see data"),
            ("upload_IQCDataCVTE6486COPY","can upload data"),
        )


class IQCUploadRecord(models.Model):
    person = models.ForeignKey(User, related_name='person_upload_record')
    upload_num = models.IntegerField(verbose_name="上传数量")
    upload_time = models.DateTimeField(auto_now_add=True, verbose_name="上传时间")

