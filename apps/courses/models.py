"""课程资料相关模型"""
from django.db import models
from datetime import datetime
from apps.organization.models import CourseOrg


class Course(models.Model):
    """课程"""
    name = models.CharField(max_length=32, verbose_name="课程名字")
    # 外键关联
    course_org = models.ForeignKey(CourseOrg, verbose_name="课程机构")
    desc = models.CharField(max_length=225, verbose_name="课程描述")
    details = models.TextField(verbose_name="课程详情")
    # 此方法避免在数据库生成多余字段，用数字代替更好
    degree_choices = ((0, "初级"), (1, "中级"), (2, "高级"))
    degree = models.IntegerField(choices=degree_choices, verbose_name="课程难度")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(分钟)")
    students = models.IntegerField(default=0, verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name="封面图")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    category = models.CharField(max_length=32, verbose_name="课程类别")
    tag = models.CharField(max_length=16, verbose_name="课程标签")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        """设置表名称"""
        verbose_name = "课程"
        # verbose_name_plural设置显示表名的复数形式，不设置会在后面加s
        verbose_name_plural = verbose_name

    def __str__(self):
        # 返回字符串的友好形式
        return self.name


class Chapter(models.Model):
    """章节"""
    course = models.ForeignKey(Course, verbose_name="课程")
    name = models.CharField(max_length=64, verbose_name="章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(models.Model):
    """配套章节视频"""
    chapter = models.ForeignKey(Chapter, verbose_name="章节")
    name = models.CharField(max_length=64, verbose_name="视频名")
    url = models.URLField(max_length=124, verbose_name="视频地址", null=True, blank=True)
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(分钟数)")
    add_time = models.DateTimeField(default=0, verbose_name="添加时间")

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    """课程资源"""
    course = models.ForeignKey(Course, verbose_name="课程")
    name = models.CharField(max_length=64, verbose_name="名称")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name="资源文件")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name