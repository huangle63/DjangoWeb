from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile


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

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
