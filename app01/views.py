from django.shortcuts import render,HttpResponse,redirect,reverse
from django.views import View
# Create your views here.
import teacher
from app01 import models
import json
from django.db.models import Q
from rbac.service.init_permission import init_permission
from app01.forms import InfoForm
from django.contrib import auth

#登录视图
class Login(View):
    def get(self,request):
        return render(request,'app01/login.html')

    def post(self,request):
        message={}
        #1.获取学号，密码,身份
        id=request.POST.get('id')
        username=request.POST.get('user')
        password=request.POST.get('pwd')

        #2.用户验证
        user=auth.authenticate(username=username,password=password,id=id)
        if not user:
            '''验证失败，返回错误信息'''
            message['message'] = '用户名或密码错误'
            return HttpResponse(json.dumps(message))

        #3.用户登陆，信息录入
        auth.login(request,user)

        #4.初始化权限信息
        init_permission(user,request)

        #5.刷新信息ajax
        message['message']='登录成功'
        return HttpResponse(json.dumps(message))

#退出视图
class Logout(View):
    def get(self,request):
        auth.logout(request)
        return redirect(reverse('app01:login'))


#首页视图
class Index(View):
    def get(self,request):
        current_user=request.user
        return render(request,'app01/index.html',{'current_user':current_user})

#个人信息
class Info(View):
    def get(self,request):
        current_user=request.user
        form_obj=InfoForm(instance=current_user)
        return render(request,'app01/info.html',{
            'form_obj':form_obj,
            'current_user':current_user,
        })

    def post(self,request):
        form_obj=InfoForm(request.POST,instance=request.user)
        if form_obj.is_valid():
            '''如果验证成功，保存并跳转首页'''
            form_obj.save()
            return redirect(reverse('app01:index'))

        '''验证失败，重新渲染信息'''
        return render(request, 'app01/info.html', {'form_obj': form_obj})

#考试安排
class Test(View):
    def get(self,request):
        '''获取所有试卷对象'''
        test_paper=teacher.models.Paper.objects.all()
        return render(request, 'app01/test.html', {
            'test_paper':test_paper,
        })

#正式考试
class TestProcess(View):
    def get(self,request,pid):
        try:
            '''获取单项选择题和主观题'''
            paper=teacher.models.Paper.objects.filter(pk=pid).first()
            paper_list_single=teacher.models.Paper.objects.filter(Q(pk=pid)&Q(status=1)).first().pid.all()
            paper_list_subject=teacher.models.Paper.objects.filter(Q(pk=pid)&Q(status=1)).first().subjective.all()
        except:
            return HttpResponse("小伙子，错过了考试，还有想法，太年轻啦")

        return render(request, 'app01/test_process.html',{
            'paper_list_single':paper_list_single,
            'paper_list_subject':paper_list_subject,
            'paper':paper,
        })

    def post(self,request,pid):
        '''尝试采用ajax获取当前试卷提交的所有单项，多选，主观题'''
        single_dict=json.loads(request.POST.get('single'))
        subject_dict=json.loads(request.POST.get('subject'))

        #试卷数据验证
        score = 0
        print(single_dict)
        paper=teacher.models.Paper.objects.get(pk=pid).pid.all()
        for single in single_dict:
            answer=paper.get(pk=single).answer          #获取正确答案
            number=paper.get(pk=single).score           #获取分值
            if answer==single_dict.get(single):
                score+=number

        return HttpResponse(json.dumps("提交成功，已自动阅卷,分数为:%s"%(score)))

#成绩查询
class Score(View):
    def get(self,request):
        score_list=models.Grade.objects.filter(sid__id=request.user.id).all()
        return render(request,'app01/score.html',{
            'score_list':score_list,
        })

#试卷开发
class Paper(View):
    def get(self,request):
        return render(request,'app01/paper.html')

#试卷编写
class WritePaper(View):
    def get(self,request):
        return render(request,'app01/writepaper.html')

#关闭考试
class ClosePaper(View):
    def get(self,request,pid):
        '''找到对应试卷,讲状态改为2(关闭)'''
        paper=teacher.models.Paper.objects.get(pk=pid)
        paper.status=2
        paper.save()
        return redirect(reverse('app01:test'))

#开启考试
class OpenPaper(View):
    def get(self,request,pid):
        '''找到对应试卷,讲状态改为1(开启)'''
        paper = teacher.models.Paper.objects.get(pk=pid)
        paper.status = 1
        paper.save()
        return redirect(reverse('app01:test'))

#回收站
class Recycle(View):
    def get(self,request):
        return render(request,"app01/recycle.html")

#文件夹
class Folder(View):
    def get(self,request):
        return render(request,"app01/folder.html")

#修改密码
class ChangePwd(View):
    def get(self,request):
        return render(request, "app01/changepwd.html")

    def post(self,request):
        former_pwd=request.POST.get("former_pwd")
        new_pwd=request.POST.get("new_pwd")
        user=request.user
        #验证密码
        if user.check_password(former_pwd):
            #如果验证成功
            user.set_password(new_pwd)
            user.save()
            return redirect(reverse("app01:index"))
        else:
            return render(request,"app01/changepwd.html",{
                "msg":"原密码输入错误"
            })
