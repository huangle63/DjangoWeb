#!/usr/bin/env python
from django.http import Http404, StreamingHttpResponse
from django.shortcuts import render, redirect

from west.models import Article
from west.tasks import build_job


# Create your views here.
def home(request):
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list' : post_list})


def detail(request, id):
    try:
        post = Article.objects.get(id = str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})


def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list,
                                             'error' : False})


def about_me(request) :
    return render(request, 'aboutme.html')


def search_tag(request, tag) :
    try:
        post_list = Article.objects.filter(category__iexact = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list})


def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'home.html')
        else:
            post_list = Article.objects.filter(title__icontains = s)
            if len(post_list) == 0 :
                return render(request,'archives.html', {'post_list': post_list,
                                                    'error': True})
            else:
                return render(request,'archives.html', {'post_list': post_list,
                                                    'error': False})
    return redirect('/')


def file_down(request):
    build_job.delay('job1', (1, 2, 3, 4))

    return redirect('/west')


# 文件下载
def file_download(request):
    # do something...
    file = "/root/20150424-315-whale-G145153.zip"
    # file = "/root/metastore.log"

    def file_iterator(file, chunk_size=512):
        with open(file, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    file_name = file.split('/')[-1].encode('utf-8')
    response = StreamingHttpResponse(file_iterator(file))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)

    return response
