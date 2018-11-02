"""用户xadmin页面管理"""
import xadmin
from xadmin import views
from .models import UserProfile, EmailVerifyRecord, Banner


class BaseSetting:
    """主题功能配置"""
    enable_themes = True
    use_bootswatch = True


class GlogbalSettings:
    """后台系统名称"""
    site_title = "幼儿园后台管理系统"
    site_footer = "幼儿园在线网"
    menu_style = "accordion"


class UserProfileAdmin:
    pass


class EmailVerifyRecordAdmin:
    # xadmin要显示得字段
    list_display = ["code", "email", "send_type", "send_time"]
    # 搜索的字段
    search_fields = ["code", "email", "send_type"]
    # 过滤的字段
    list_filter = ["code", "email", "send_type", "send_time"]


class BannerAdmin:
    list_display = ["title", "image", "url", "index", "add_time"]
    search_fields = ["title", "image", "send_type"]
    list_filter = ["title", "image", "url", "index", "add_time"]


# 注册
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlogbalSettings)
