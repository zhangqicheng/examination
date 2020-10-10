from django.shortcuts import render,HttpResponse,redirect,reverse
from django.views import View
# Create your views here.
from app01 import models
import json
from django.db.models import Q

#登录视图
class Login(View):
    def get(self,request):
        return render(request,'app01/login.html')

    def post(self,request):
        message={}
        #1.获取学号，密码
        student_id=request.POST.get('user')
        password=request.POST.get('pwd')

        #2.访问数据库验证,获取对象
        objects=models.Student.objects.filter(Q(pk=student_id)&Q(password=password)).first()
        if objects:
            message['message']='登录成功'
            return HttpResponse(json.dumps(message))
        else:
            message['message']='用户名或密码错误'
            return HttpResponse(json.dumps(message))

#首页视图
class Index(View):
    def get(self,request):
        return render(request,'app01/index.html')
