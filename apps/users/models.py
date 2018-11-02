"""用户相关的模型表"""
from django.db import models
from django.contrib.auth.models import AbstractUser     # 导入auth-user模块
from datetime import datetime


class UserProfile(AbstractUser):
    """继承django模块AbstractBaseUser并扩展"""
    nick_name = models.CharField(max_length=32, default="", verbose_name="昵称")
    # null针对数据库字段可以为空，blank表单填写时可以为空
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    # 此方法避免在数据库生成多余字段，用数字代替更好
    gender_choices = ((1, "男"), (2, "女"))
    gender = models.IntegerField(choices=gender_choices, default=1, verbose_name="性别")
    address = models.CharField(max_length=64, default="", verbose_name="居住地址")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name="手机号码")
    # upload_to指明文件的路径（image/年/月）
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png", verbose_name="头像")

    class Meta:
        """设置表名称"""
        verbose_name = "用户信息"
        # verbose_name_plural设置显示表名的复数形式，不设置会在后面加s
        verbose_name_plural = verbose_name

    def __str__(self):
        # 返回字符串的友好方式
        return self.username


class EmailVerifyRecord(models.Model):
    """邮箱验证"""
    code = models.CharField(max_length=32, verbose_name="验证码")
    email = models.EmailField(max_length=64, verbose_name="邮箱")
    send_type_choices = ((0, "注册"), (1, "找回密码"), (2, "修改邮箱"))
    send_type = models.IntegerField(choices=send_type_choices, verbose_name="类别")
    send_time = models.DateField(default=datetime.now, verbose_name="发送时间")

    class Meta:
        """设置表名称"""
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email


class Banner(models.Model):
    """轮播图"""
    title = models.CharField(max_length=64, verbose_name="标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name="轮播图")
    url = models.URLField(max_length=225, verbose_name="访问地址")
    index = models.IntegerField(default=99, verbose_name="顺序")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
