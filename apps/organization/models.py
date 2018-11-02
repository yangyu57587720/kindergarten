"""课程体系相关模型表"""
from django.db import models
from datetime import datetime


class CityDict(models.Model):
    """城市"""
    name = models.CharField(max_length=32, verbose_name="城市名")
    desc = models.CharField(max_length=225, verbose_name="城市描述")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        # 设置表名称
        verbose_name = "城市"
        # verbose_name_plural设置显示表名的复数形式，不设置会在后面加s
        verbose_name_plural = verbose_name

    def __str__(self):
        # 返回字符串的友好形式
        return self.name


class CourseOrg(models.Model):
    """课程机构"""
    name = models.CharField(max_length=32, verbose_name="机构名称")
    desc = models.TextField(verbose_name="机构描述")
    # 此方法避免在数据库生成多余字段，用数字代替更好
    category_choices = ((0, "机构"), (1, "个人"), (2, "高校"))
    category = models.IntegerField(choices=category_choices, verbose_name="类别")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    image = models.ImageField(upload_to="organization/%Y/%m", verbose_name="封面图")
    address = models.CharField(max_length=225, verbose_name="机构地址")
    # 外键关联
    city = models.ForeignKey(CityDict, verbose_name="所在城市")
    students = models.IntegerField(default=0, verbose_name="学习人数")
    course_nums = models.IntegerField(default=0, verbose_name="课程数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name

    def get_teacher_nums(self):
        # 获取教师数，反向取值表名小写_set
        return self.teacher_set.count()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    """教师"""
    org = models.ForeignKey(CourseOrg, verbose_name="所属机构")
    name = models.CharField(max_length=32, verbose_name="教室名字")
    age = models.IntegerField(default=18, verbose_name="年龄")
    image = models.ImageField(upload_to="teacher/%Y/%m", verbose_name="头像")
    work_years = models.IntegerField(default=0, verbose_name="工作年限")
    work_company = models.CharField(max_length=32, verbose_name="就职公司")
    work_position = models.CharField(max_length=32, verbose_name="公司职位")
    points = models.TextField(verbose_name="教学特点")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
