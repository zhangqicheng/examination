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
        #1.获取学号，密码,身份
        number=request.POST.get('user')
        password=request.POST.get('pwd')
        check=request.POST.get('check')

        #2.根据登录身份，获取当前用户对象
        if check=='student':
            current_user = models.Student.objects.filter(Q(pk=number) & Q(password=password)).first()
        else:
            current_user = models.Teacher.objects.filter(Q(pk=number) & Q(password=password)).first()

        if not current_user:
            message['message'] = '用户名或密码错误'
            return HttpResponse(json.dumps(message))

        """
        如正确，根据当前用户获取所有权限信息,并放入session
        """
        #3.获取当前用户权限信息
        permission_query=current_user.roles.filter(permissions__isnull=False).values('permissions__title','permissions__url').distinct()
        permission_list=[permission['permissions__url'] for permission in permission_query]

        #4.将权限信息放入session中
        request.session['qicheng']=permission_list

        #最后刷新信息给ajax
        message['message']='登录成功'
        return HttpResponse(json.dumps(message))


#首页视图
class Index(View):
    def get(self,request):
        return render(request,'app01/index.html')

#个人信息
class Info(View):
    def get(self,request):
        return HttpResponse('个人信息')

#考试安排
class Test(View):
    def get(self,request):
        return HttpResponse('考试安排')

#成绩查询
class Score(View):
    def get(self,request):
        return HttpResponse('成绩查询')