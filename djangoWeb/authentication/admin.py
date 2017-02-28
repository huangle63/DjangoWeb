from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile
from ..iqc.models import IQCDataCVTE6486COPY


'''
如果只注册模型，
①注册一个模型，admin.site.register(Character)；
②注册多个模型，admin.site.register([Character, Tag])；
如果模型有自己新增的展示列，需要单独注册，
admin.site.register(Character, CharacterAdmin)
'''


# Register your models here.
# Define an inline admin descriptor for Extend model
# which acts a bit like a singleton
class ExtendInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = '扩展信息'


# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ExtendInline, )


class IQCDataCVTE6486COPYAdmin(admin.ModelAdmin):
    list_display = ('id', 'tm', 'scpc','cssj')

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(IQCDataCVTE6486COPY,IQCDataCVTE6486COPYAdmin)