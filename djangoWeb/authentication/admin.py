from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile
from ..iqc.models import IQCDataCVTE6486COPY, IQCUploadRecord
from ..gyhandover.models import GYHandover
from ..jiradata.models import JiraSearchRecord, JiraDownloadRecord


'''
如果只注册模型，
①注册一个模型，admin.site.register(Character)；
②注册多个模型，admin.site.register([Character, Tag])；
如果模型有自己新增的展示列，需要单独注册，
admin.site.register(Character, CharacterAdmin)
'''

'''
User 模型
'''
# Register your models here.
# Define an inline admin descriptor for Extend model
# which acts a bit like a singleton
class UserExtendInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = '扩展信息'


# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserExtendInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

'''
IQC 模型
'''
class IQCDataCVTE6486COPYAdmin(admin.ModelAdmin):
    list_display = ('id', 'tm', 'scpc','cssj')


class IQCUploadRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'person', 'upload_num','upload_time')

# Re-register UserAdmin
admin.site.register(IQCDataCVTE6486COPY,IQCDataCVTE6486COPYAdmin)
admin.site.register(IQCUploadRecord, IQCUploadRecordAdmin)


'''
JIRA 模型
'''
class JiraSearchRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'project_id','model', 'download_id', 'search_time')
    search_fields = ['username']


class JiraDownloadRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'search_record_username', 'search_record_project_id', 'search_record_model', 'search_record_download_id', 'download_time')

    def search_record_username(self, obj):
        return obj.search_record.username

    def search_record_project_id(self, obj):
        return obj.search_record.project_id

    def search_record_model(self, obj):
        return obj.search_record.model

    def search_record_download_id(self, obj):
        return obj.search_record.download_id

    search_record_username.short_description = "姓名"
    search_record_project_id.short_description = "项目编号"
    search_record_model.short_description = "机型"
    search_record_download_id.short_description = "下载链接"

# Re-register UserAdmin
admin.site.register(JiraSearchRecord, JiraSearchRecordAdmin)
admin.site.register(JiraDownloadRecord, JiraDownloadRecordAdmin)