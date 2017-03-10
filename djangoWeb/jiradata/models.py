from django.db import models


# Create your models here.
class JiraSearchRecord(models.Model):
    username = models.CharField(max_length=50, verbose_name="姓名")
    project_id = models.CharField(max_length=50, verbose_name="项目编号")
    model = models.CharField(max_length=200, verbose_name="机型")
    download_id = models.CharField(max_length=50, verbose_name="下载链接")
    search_time = models.DateTimeField(auto_now_add=True, verbose_name="查询时间")

    # python2使用__unicode__, python3使用__str__
    def __str__(self):
        return self.username


class JiraDownloadRecord(models.Model):
    search_record = models.ForeignKey(JiraSearchRecord, related_name='search_record')
    download_time = models.DateTimeField(auto_now_add=True, verbose_name="下载时间")



