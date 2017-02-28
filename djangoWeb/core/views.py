from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
import json

from .forms import ProfileForm, ChangePasswordForm


# Create your views here.
def home(request):
    return render(request, 'core/home.html')


# 登录函数
# def loginform(request):
#     return render(request, 'core/login.html')
    # if request.method == 'POST':
    #     username = request.POST.get('form_email')
    #     password = request.POST.get('form_password')
    #     user = authenticate(username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return render(request, 'core/home.html')
    #     else:
    #         # return HttpResponse('用户名密码错误')
    #         return render(request, 'core/login.html')
    # else:
    #     return render(request, 'core/login.html')


# 登录函数
def login_form(request):
    if request.method == 'POST':
        # dataReceiveJson = request.POST.get('dataJson')  # 数据类型格式为str
        # res = json.loads(dataReceiveJson)  # 数据类型格式为dict
        # username = res['email']
        # password = res['password']
        username = request.POST.get('form_email')
        password = request.POST.get('form_password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('登录成功')
        else:
            return HttpResponse('invalid user')
            # return HttpResponse(json.dumps(res))
    else:
        return render(request, 'core/login.html')


# 检查用户名是否存在
def validate_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        result = {'resultCode': 1,'message': ''}
        if User.objects.filter(username__iexact=username).exists():
            result['resultCode'] = 1
            result['message'] = '用户名已存在'
            return HttpResponse(json.dumps(result))
        else:
            result['resultCode'] = 0
            result['message'] = '用户名可以使用'
            return HttpResponse(json.dumps(result))


# 检查邮箱是否存在
def validate_email(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        result = {'resultCode': 1,'message': ''}
        if User.objects.filter(username__iexact=username).exists():
            result['resultCode'] = 1
            result['message'] = '此邮箱已存在'
            return HttpResponse(json.dumps(result))
        else:
            result['resultCode'] = 0
            result['message'] = '邮箱可以使用'
            return HttpResponse(json.dumps(result))


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
        dataReceiveJson = request.POST.get('dataJson')    #数据类型格式为str
        res = json.loads(dataReceiveJson)                  #数据类型格式为dict
        username = res['username']
        password = res['password']
        return HttpResponse(json.dumps(res))



