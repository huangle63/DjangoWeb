from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils.translation import ugettext_lazy as _

from .forms import SignUpForm

# Create your views here.
def signup(request):
    if request.method != 'POST':
        return render(request, 'auth/signup.html', {'form': SignUpForm()})
    # form类的运行顺序是init，clean，validte，save
    # 其中init,clean和validate会在form.is_valid()方法中被先后调用
    form = SignUpForm(request.POST)

    if not form.is_valid():
        return render(request, 'auth/signup.html', {'form': form})

    email = form.cleaned_data.get('email')
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password')

    User.objects.create_user(username=username, password=password,
                             email=email)
    user = authenticate(username=username, password=password)
    login(request, user)

    welcome_post = _('{0} has joined the network.').format(user.username)
    # Feed.objects.create(user=user, post=welcome_post)

    return redirect('/')