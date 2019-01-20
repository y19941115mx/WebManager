from django.contrib import admin
from .models import *
# Register your models here.


class BannerAdmin(admin.ModelAdmin):
    empty_value_display = '-空-'
    date_hierarchy = 'add_time'

    list_display = ('type', 'desc', 'add_time',)#要显示的字段名


admin.site.register(Banner, BannerAdmin)
