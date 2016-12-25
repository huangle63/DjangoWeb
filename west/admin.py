from django.contrib import admin
from west.models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'date_time', 'content')

'''
如果只注册模型，
①注册一个模型，admin.site.register(Character)；
②注册多个模型，admin.site.register([Character, Tag])；
如果模型有自己新增的展示列，需要单独注册，
admin.site.register(Character, CharacterAdmin)
'''

admin.site.register(Article, ArticleAdmin)