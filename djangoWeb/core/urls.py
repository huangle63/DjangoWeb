from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.settings, name='settings'),
    url(r'^password/$', views.password, name='password'),
    url(r'^t', views.t, name="t"),
    url(r'^validate_username', views.validate_user, name="validate_user"),
    url(r'^validate_email', views.validate_email, name="validate_email"),

]