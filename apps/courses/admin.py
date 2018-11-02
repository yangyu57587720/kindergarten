"""课程资料相关xadmin"""
import xadmin
from .models import Course, Chapter, Video, CourseResource


class CourseAdmin:
    # xadmin要显示得字段
    list_display = ["name", "desc", "degree", "learn_times", "students", "fav_nums", "image", "click_nums", "add_time"]
    # 搜索的字段
    search_fields = ["name", "desc", "degree", "learn_times", "students", "fav_nums", "click_nums"]
    # 过滤的字段
    list_filter = ["name", "desc", "degree", "students", "fav_nums", "image", "click_nums", "add_time"]


class ChapterAdmin:
    list_display = ["course", "name", "add_time"]
    search_fields = ["course", "name"]
    list_filter = ["course__name", "name", "add_time"]


class VideoAdmin:
    list_display = ["chapter", "name", "add_time"]
    search_fields = ["chapter", "name"]
    list_filter = ["chapter__name", "name", "add_time"]


class CourseResourceAdmin:
    list_display = ["course", "name", "download", "add_time"]
    search_fields = ["course", "name", "download"]
    list_filter = ["course__name", "name", "add_time"]


# 注册
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(Chapter, ChapterAdmin)
xadmin.site.register(Video, VideoAdmin)