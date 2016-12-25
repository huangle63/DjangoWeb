from django.shortcuts import render
from django.http import HttpResponse
from west.models import Article

# Create your views here.
def west_home(request):
    return HttpResponse("West Home Page")

def detail(request, my_args):
    post = Article.objects.get(id = int(my_args))
    str = ("title = %s, category = %s, date_time = %s, content = %s"
           %(post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)