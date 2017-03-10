from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^search-data/', views.search_data, name='jira-search-data'),
    url(r'^import-record/', views.import_record, name='jira-import-record'),
    url(r'^download/', views.file_download),

]