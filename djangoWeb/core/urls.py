from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.settings, name='settings'),
    url(r'^password/$', views.password, name='password'),
    url(r'^t', views.t, name="t"),
]