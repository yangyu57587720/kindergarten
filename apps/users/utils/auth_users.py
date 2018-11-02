from django.contrib.auth.backends import ModelBackend
from apps.users.models import UserProfile


class CustomBackend(ModelBackend):
    """重写认证方法"""
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 判断用户名
            user = UserProfile.objects.get(username=username)
            # 检查明文密码
            if user.check_password(password):
                return user
        except Exception as e:
            return None
