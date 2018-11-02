"""用户相关信息xadmin"""
import xadmin
from .models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse


class UserAskAdmin:
    # xadmin要显示得字段
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    # 搜索的字段
    search_fields = ['name', 'mobile', 'course_name']
    # 过滤的字段
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


class CourseCommentsAdmin:
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user__nick_name', 'course__name', 'comments', 'add_time']


class UserFavoriteAdmin:
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user__nick_name', 'fav_id', 'fav_type', 'add_time']


class UserMessageAdmin:
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class UserCourseAdmin:
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course', 'add_time']
    list_filter = ['user__nick_name', 'course__name', 'add_time']


# 注册
xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
