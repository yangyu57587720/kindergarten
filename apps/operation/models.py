"""用户相关信息记录模型"""
from django.db import models
from datetime import datetime
from apps.users.models import UserProfile
from apps.courses.models import Course


class UserAsk(models.Model):
    """用户咨询"""
    name = models.CharField(max_length=32, verbose_name="姓名")
    mobile = models.CharField(max_length=11, verbose_name="手机号码")
    course_name = models.CharField(max_length=64, verbose_name="课程名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseComments(models.Model):
    """课程评论"""
    user = models.ForeignKey(UserProfile, verbose_name="用户")
    # 建立外键关联
    course = models.ForeignKey(Course, verbose_name="课程")
    comments = models.CharField(max_length=225, verbose_name="评论")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comments


class UserFavorite(models.Model):
    """用户收藏"""
    user = models.ForeignKey(UserProfile, verbose_name="用户")
    fav_id = models.IntegerField(default=0, verbose_name="数据id")
    # 此方法避免在数据库生成多余字段，用数字代替更好
    fav_choices = ((0, "课程"), (1, "机构"), (2, "讲师"))
    fav_type = models.IntegerField(choices=fav_choices, verbose_name="收藏类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    """用户消息"""
    user = models.IntegerField(default=0, verbose_name="接收用户")
    message = models.TextField(verbose_name="消息内容")
    # 返回布尔值数据True/False
    has_read = models.BooleanField(default=False, verbose_name="是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message


class UserCourse(models.Model):
    """用户课程"""
    user = models.ForeignKey(UserProfile, verbose_name="用户")
    course = models.ForeignKey(Course, verbose_name="课程")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户课程"
        verbose_name_plural = verbose_name


