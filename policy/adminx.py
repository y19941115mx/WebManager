from .models import *
import xadmin
from xadmin import views
# Register your models here.


@xadmin.sites.register(views.BaseAdminView)
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


@xadmin.sites.register(views.CommAdminView)
class GlobalSetting(object):
    site_title = '江淮政策云系统管理后台'
    site_footer = '江淮政策云'


class PolicyCardInline(object):
    model = PolicyCard
    extra = 1


# @xadmin.sites.register(Policy)
# class PolicyAdmin(object):
#     inlines = [PolicyCardInline]

#     show_bookmarks = False

#     list_display = ('policy_title', 'policy_id', 'add_time')
#     list_display_links = ("policy_title",)

#     list_filter = ['policy_title', 'policy_id', 'add_time']
#     search_fields = ['policy_title', 'policy_id']
#     # style_fields = {"hosts": "checkbox-inline"}


@xadmin.sites.register(PolicyCard)
class PolicyCardAdmin(object):
    show_bookmarks = False
    list_display = ('policy_id', 'title', 'end_time', 'add_time')
    list_display_links = ("title",)
    list_filter = ["title", 'end_time', 'add_time']
    search_fields = ["title", 'policy_id']





