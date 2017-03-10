from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# 工艺部夜班交接
class GYHandover(models.Model):
    # person = models.ForeignKey(User, related_name='person_upload_record')
    # section lk= models.CharField(max_length=100, verbose_name="科室")
    # comment = models.CharField(max_length=1000, verbose_name="备注")
    handover_img = models.ImageField(upload_to='./image/gyhandover/%Y/%m', verbose_name="附件图片")
    upload_time = models.DateTimeField(auto_now_add=True, verbose_name="上传时间")

    class Meta:
        ordering = ['upload_time']
