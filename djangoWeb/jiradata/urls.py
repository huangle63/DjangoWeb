from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^search-data/', views.search_data, name='jira-search-data'),
    url(r'^download/', views.file_download),

]