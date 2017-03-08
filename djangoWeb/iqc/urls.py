from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^upload-data/', views.upload_data, name='iqc-upload-data'),
    url(r'^search-data/', views.search_data, name='iqc-search-data'),
    url(r'^timeline/', views.iqc_timeline, name='iqc-timeline'),
]