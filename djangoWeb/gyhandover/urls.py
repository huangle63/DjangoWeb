from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^uploadimg/', views.upload_img, name='gy-uploadimg'),
    url(r'^showimg/', views.show_img, name='gy-showimg'),
]