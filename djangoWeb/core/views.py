from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
import json

from .forms import ProfileForm, ChangePasswordForm


# Create your views here.
def home(request):
    return render(request, 'core/home.html')


@login_required
def profile(request, username):
    if request.user.username != username:
        return render(request, '404.html')
    # get_object_or_404 会默认的调用django 的get方法，
    # 如果查询的对象不存在的话，会抛出一个Http404的异常
    page_user = get_object_or_404(User, username=username)
    context = {
        'page_user': page_user
    }
    return render(request, 'core/profile.html', context)


@login_required
def settings(request):
    user = request.user
    print(user.username)
    if request.method == 'POST':
        pass
    else:
        initial = {
            'job_title': user.profile.job_title,
            'url': user.profile.url,
            'location': user.profile.location
        }
        form = ProfileForm(instance=user, initial=initial)

    return render(request, 'core/settings.html', {'form': form})


@login_required
def password(request):
    user = request.user
    if request.method == 'POST':
        pass
    else:
        form = ChangePasswordForm(instance=user)

        return render(request, 'core/password.html', {'form': form})


def test(request):
    return render(request, 'core/test.html')


def t(request):
    if request.method == 'GET':
        a = request.GET.get('a', '')
        b = request.GET.get('b', '')
        return HttpResponse(a + 'bbb')
    elif request.method == 'POST':
        dataJson = request.POST.get('dataJson')    #数据类型格式为str
        res = json.loads(dataJson)                  #数据类型格式为dict
        return HttpResponse(json.dumps(res))

