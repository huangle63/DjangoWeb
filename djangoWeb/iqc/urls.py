from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^upload-data/', views.upload_data, name='upload-data'),
    url(r'^search-data/', views.search_data, name='search-data'),

]