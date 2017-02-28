"""djangoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from djangoWeb.core import views as core_views
from djangoWeb.authentication import views as authentication_views

# admin的超级用户 用户名：huangle63，邮箱:huangle63@163.cmo,密码：Software123
# 普通用户letu，密码123
# 普通用户lele，密码123456qwe
'''
url(regex, view, [kwargs, name])函数有四个参数, 两个是必须的:regex和view, 两个可选的:kwargs和name
regex是regular expression的简写,这是字符串中的模式匹配的一种语法, Django 将请求的URL从上至下依次匹配列表中的正则表达式，直到匹配到一个为止。 更多正则表达式的使用可以查看Python正则表达式
view当 Django匹配了一个正则表达式就会调用指定的view逻辑, 上面代码中会调用article/views.py中的home函数
kwargs任意关键字参数可传一个字典至目标view
name命名你的 URL, 使url在 Django 的其他地方使用, 特别是在模板中
'''
urlpatterns = [
    # ^ 匹配字符串开头, $ 匹配字符串末尾,
    url(r'^admin/', admin.site.urls),   #可以使用设置好的url进入网站后台
    url(r'^$', core_views.home, name='home'),             #匹配空
    # url(r'^login/$', auth_views.login, {'template_name': 'core/login.html'},
    #     name='login'),
    url(r'^login/$', core_views.login_form,name='login'),
    url(r'^signup/$', authentication_views.signup, name='signup'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^settings/', include('djangoWeb.core.urls')),
    url(r'^validate/', include('djangoWeb.core.urls')),
    url(r'^iqc/',include('djangoWeb.iqc.urls')),
    url(r'^jira/',include('djangoWeb.jiradata.urls')),
    url(r'^test/',core_views.test, name='test'),
    url(r'^(?P<username>[^/]+)/$', core_views.profile, name='profile'),


    url(r'^west/', include('djangoWeb.west.urls')),
]
