from django.conf.urls import url
from west import views

'''
^(?P<my_args>\d+)/$这个正则表达式的意思是将传入的一位或者多位数字作为参数传递到views中的detail作为参数,
其中?P<my_args>定义名称用于标识匹配的内容
'''
urlpatterns = [
    url(r'^$', views.west_home),
    url(r'^(?P<my_args>\d+)/$', views.detail),
]