from django.shortcuts import render,HttpResponse,redirect,reverse
from django.views import View
# Create your views here.
from app01 import models
import json
from django.db.models import Q
from rbac.service.init_permission import init_permission
from app01.forms import InfoForm

#登录视图
class Login(View):
    def get(self,request):
        return render(request,'app01/login.html')

    def post(self,request):
        message={}
        #1.获取学号，密码,身份
        number=request.POST.get('user')
        password=request.POST.get('pwd')
        check=request.POST.get('check')

        #2.登录
        if check=='student':
            current_user = models.Student.objects.filter(Q(pk=number) & Q(password=password)).first()
        else:
            current_user = models.Teacher.objects.filter(Q(pk=number) & Q(password=password)).first()

        if not current_user:
            message['message'] = '用户名或密码错误'
            return HttpResponse(json.dumps(message))

        #3.初始化权限信息
        init_permission(current_user,request)

        #刷新信息ajax
        message['message']='登录成功'
        return HttpResponse(json.dumps(message))


#首页视图
class Index(View):
    def get(self,request):
        return render(request,'app01/index.html')

#个人信息
class Info(View):
    def get(self,request):
        form=InfoForm()
        return render(request,'app01/info.html',{'form':form})

#考试安排
class Test(View):
    def get(self,request):
        return HttpResponse('考试安排')

#成绩查询
class Score(View):
    def get(self,request):
        return HttpResponse('成绩查询')