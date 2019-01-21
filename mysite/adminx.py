from .models import *
import xadmin
from xadmin import views
# Register your models here.


# class PolicyCardAdmin(object):
#     empty_value_display = '-空-'
#     date_hierarchy = 'add_time'
#
#     list_display = ('policy', 'title', 'apply_time', 'add_time')#要显示的字段名

@xadmin.sites.register(views.BaseAdminView)
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


@xadmin.sites.register(views.CommAdminView)
class GlobalSetting(object):
    site_title = '江淮政策云系统管理后台'
    site_footer = '江淮政策云'
    menu_style = 'default'  # 'accordion'


class PolicyInline(object):
    model = Policy
    extra = 1
    # style = "accordion"


@xadmin.sites.register(PolicyCard)
class HostGroupAdmin(object):
    inlines = [PolicyInline]

    list_display = ('title', 'apply_time', 'add_time')
    list_display_links = ( "title",)
    list_filter = ["title"]
    search_fields = ["title"]
    # style_fields = {"hosts": "checkbox-inline"}





