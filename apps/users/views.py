import json
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login


class LoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        res = {"state_code": 1000, "msg": None}
        try:
            name = request.data.get("name")
            pwd = request.data.get("pwd")
            user = authenticate(username=name, password=pwd)
            if user:
                login(request, user)
                return redirect("index.html")
            else:
                res["state_code"] = 1001
                res["msg"] = "用户名或密码错误"
                return render(request, "login.html", {"res": res})
        except Exception as e:
            res["msg"] = "意外错误，断开连接"
            return Response(json.dumps(res, ensure_ascii=False))

