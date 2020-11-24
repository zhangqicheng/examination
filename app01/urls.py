"""examination URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from app01.views import Login,Logout,Index,Info,Test,Score,Paper,TestProcess,ClosePaper,OpenPaper,\
    WritePaper,Recycle,Folder,ChangePwd

urlpatterns = [
    path('login/',Login.as_view(),name='login'),         #登录
    path('logout/',Logout.as_view(),name='logout'),      #退出
    path('index/',Index.as_view(),name='index'),         #首页
    path('info/',Info.as_view(),name='info'),            #个人信息
    path('test/',Test.as_view(),name='test'),            #考试安排
    re_path('test/process/(\d+)/',TestProcess.as_view(),name='testprocess'),     #正式考试
    path('score/',Score.as_view(),name='score'),          #成绩查询
    path('paper/',Paper.as_view(),name='paper'),          #试卷开发
    path('writepaper/',WritePaper.as_view(),name='writepaper'),    #编写试卷
    re_path('closepaper/(\d+)/',ClosePaper.as_view(),name='closepaper'),     #关闭试卷
    re_path('openpaper/(\d+)/',OpenPaper.as_view(),name='openpaper'),        #开启试卷
    path('recycle/',Recycle.as_view(),name="recycle"),     #回收站
    path('folder/',Folder.as_view(),name="folder"),      #文件夹
    path('changepwd/',ChangePwd.as_view(),name="changepwd"), #修改密码
]