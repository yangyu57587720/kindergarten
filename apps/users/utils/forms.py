"""form注册模块"""
import re
from django import forms
from django.core.exceptions import ValidationError


def mobile_validate(value):
    # 自定义效验手机号码
    mobile = re.compile(r"^1(?:3\d|4[4-9]|5[0-35-9]|6[67]|7[013-8]|8\d | 9\d)\d{8}$")
    if not mobile.match(value):
        raise ValidationError("手机号码格式错误")


class RegisterForm(forms.Form):
    username = forms.CharField(
        min_length=8,
        label="用户名",
        error_messages={
            "required": "用户名不能为空",
            "invalid": "用户名格式错误",
            "min_length": "用户名最短8位",
        },
        widget=forms.widgets.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        min_length=8,
        label="密码",
        error_messages={
            "required": "密码不能为空",
            "invalid": "密码格式错误",
            "min_length": "密码最短8位",
        },
        widget=forms.widgets.PasswordInput(
            attrs={"class": "form-control"},
            render_value=True,
        ),
    )
    re_password = forms.CharField(
        min_length=8,
        label="确认密码",
        error_messages={
            "required": "确认密码不能为空",
            "invalid": "确认密码格式错误",
            "min_length": "两次密码不一致",
        },
        widget=forms.widgets.PasswordInput(attrs={"class": "form-control"}, render_value=True)
    )
    # 使用自定义手机号码验证规则
    phone = forms.CharField(
        label="手机号码",
        validators=[mobile_validate],
        error_messages={"required": "手机号码不能为空"},
        widget=forms.widgets.TextInput(attrs={"class": "form-control"})
    )
    # 应用form组件自带邮箱验证
    email = forms.EmailField(
        label="邮箱",
        error_messages={
            "required": u"邮箱不能为空",
            "invalid": u"邮箱格式错误",
        },
        widget=forms.widgets.TextInput(attrs={"class": "form-control"})
    )

    # 重写全局的钩子函数,对确认密码做效验
    def clean(self):
        password = self.cleaned_data.get("password")
        re_password = self.changed_data.get("re_password")

        if re_password and re_password != password:
            self.add_error("re_password", ValidationError("两次密码不一致"))
        else:
            return self.changed_data


