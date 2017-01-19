from django.conf.urls import url

from djangoWeb.west import views

'''
^(?P<my_args>\d+)/$这个正则表达式的意思是将传入的一位或者多位数字作为参数传递到views中的detail作为参数,
其中?P<my_args>定义名称用于标识匹配的内容
'''
urlpatterns = [
    url(r'^$', views.home, name='west_home'),
    url(r'^(?P<id>\d+)/$', views.detail, name='west_detail'),
    url(r'^archives/$', views.archives, name ='west_archives'),
    url(r'^aboutme/$', views.about_me, name ='west_about_me'),
    url(r'^tag(?P<tag>\w+)/$', views.search_tag, name ='west_search_tag'),
    url(r'^search/$', views.blog_search, name ='west_search'),
    url(r'download', views.file_down, name ='west_file_download'),
]