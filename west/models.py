#!/usr/bin/env python3

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Article(models.Model) :
    title = models.CharField(max_length = 100)  #博客题目
    category = models.CharField(max_length = 50, blank = True)  #博客标签
    date_time = models.DateTimeField(auto_now_add = True)  #博客日期,auto_now_add设置True表示自动设置对象增加时间
    content = models.TextField(blank = True, null = True)  #博客文章正文

    # 获取URL并转换成url的表示格式
    def get_absolute_url(self):
        path = reverse('west_detail', kwargs={'id': self.id})
        return "http://127.0.0.1:8000%s" % path

    #python2使用__unicode__, python3使用__str__
    def __str__(self) :
        return self.title

    class Meta:  #按时间下降排序
        ordering = ['-date_time']