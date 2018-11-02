import json
from django.shortcuts import render, redirect, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from geetest import GeetestLib
from apps.users.utils.auth_users import CustomBackend
from apps.users.utils.forms import RegisterForm
from apps.users import models


class RegisterView(APIView):
    """注册"""
    def get(self, request):
        form_obj = RegisterForm()
        return render(request, "register.html", {"form_obj": form_obj})

    def post(self, request):
        res = {"status": 1000, "msg": None}
        try:
            # 实例化form对象的时候，把post提交过来的数据直接传进去
            form_obj = RegisterForm(request.POST)
            # 调用form_obj校验数据
            if form_obj.is_valid():
                # 删除已效验的再次确认密码
                form_obj.cleaned_data.pop("re_password")
                image_img = request.FILES.get("image")
                models.UserProfile.objects.create_user(**form_obj.cleaned_data, image=image_img)
                res["msg"] = "/index/"
                return JsonResponse(res)
            else:
                res["status"] = 1002
                res["msg"] = form_obj.errors
                return JsonResponse(res)
        except Exception as e:
            res["status"] = 1002
            res["msg"] = "意外错误，断开连接"
            return Response(json.dumps(res, ensure_ascii=False))


class LoginView(APIView):
    """登录"""
    authentication_classes = [CustomBackend]    # 认证
    permission_classes = []                     # 权限

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        res = {"status": 1000, "msg": None}
        try:
            name = request.data.get("name")
            pwd = request.data.get("pwd")
            # 获取极验 滑动验证码相关的参数
            gt = GeetestLib(pc_geetest_id, pc_geetest_key)
            challenge = request.POST.get(gt.FN_CHALLENGE, '')
            validate = request.POST.get(gt.FN_VALIDATE, '')
            seccode = request.POST.get(gt.FN_SECCODE, '')
            status = request.session[gt.GT_STATUS_SESSION_KEY]
            user_id = request.session["user_id"]

            if status:
                result = gt.success_validate(challenge, validate, seccode, user_id)
            else:
                result = gt.failback_validate(challenge, validate, seccode)
            if result:
                # 对比数据表的的账号和密码
                user = authenticate(username=name, password=pwd)
                if user:
                    login(request, user)   # 使用login模块进行登录
                    return redirect("index")
                else:
                    res["status"] = 1001
                    res["msg"] = "用户名或密码错误"
            else:
                res["status"] = 1001
                res["msg"] = "验证码错误"
            return JsonResponse(res)
        except Exception as e:
            res["msg"] = "意外错误，断开连接"
            return Response(json.dumps(res, ensure_ascii=False))


class IndexView(APIView):
    """首页"""
    def get(self, request):
        return render(request, "index.html")

    def post(self, request):
        pass


# 请在官网申请ID使用，示例ID不可使用
pc_geetest_id = "17b419676702716d38b2b510f756b28f"
pc_geetest_key = "e7b74db355df3b0ddc5c2960f45853fa"


# 处理极验 获取验证码的视图
def get_geetest(request):
    user_id = 'test'
    gt = GeetestLib(pc_geetest_id, pc_geetest_key)
    status = gt.pre_process(user_id)
    request.session[gt.GT_STATUS_SESSION_KEY] = status
    request.session["user_id"] = user_id
    response_str = gt.get_response_str()
    return HttpResponse(response_str)