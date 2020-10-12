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
from app01.views import Login,Index,Info,Test,Score

urlpatterns = [
    path('login/',Login.as_view(),name='login'),         #登录
    path('index/',Index.as_view(),name='index'),         #首页
    path('info/',Info.as_view(),name='info'),            #个人信息
    path('test/',Test.as_view(),name='test'),            #考试安排
    path('score/',Score.as_view(),name='score'),          #成绩查询
]