from django.db import models
from rbac.models import Role,UserInfo
from django.contrib.auth.models import AbstractUser
import teacher
# Create your models here.
Sex=(
        ('男','男'),
        ('女','女'),
        ('中性','中性')
    )
Dept=(
    ('计算机与通信学院', '计算机与通信学院'),
    ('电气与自动化学院', '电气与自动化学院'),
    ('外国语学院', '外国语学院'),
    ('理学院', '理学院'),
    ('土木工程学院','土木工程学院'),
)

#学院信息表
class Institute(models.Model):
    name=models.CharField('学院名称',max_length=64,null=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name='学院信息表'
        verbose_name_plural=verbose_name
        db_table='institute'
        unique_together=(
            ('name',)
        )

#专业信息表
class Profession(models.Model):
    iid=models.ForeignKey(verbose_name='学院名称',to=Institute,on_delete=models.CASCADE,default='')
    career=models.CharField(verbose_name='专业名称',max_length=64,null=True)

    def __str__(self):
        return self.career

    class Meta():
        verbose_name='专业信息表'
        verbose_name_plural=verbose_name
        db_table='profession'
        unique_together=(
            ('career',)
        )

#用户表
class UserProfile(AbstractUser,UserInfo):
    id=models.CharField(verbose_name='学号',max_length=16,primary_key=True)
    username=models.CharField(verbose_name='姓名',max_length=32,unique=True)
    password = models.CharField(verbose_name='密码', max_length=128, default='123')
    sex=models.CharField(verbose_name='性别',max_length=8,choices=Sex,default='中性')
    academy=models.ForeignKey(verbose_name='所在学院',to=Institute,on_delete=models.CASCADE,null=True,default='')
    profession=models.ForeignKey(verbose_name='所在专业',to=Profession,on_delete=models.CASCADE,null=True,default='')
    birth=models.DateField(verbose_name='出生日期',auto_created=True,null=True)
    roles=models.ManyToManyField(to=Role,null=True,blank=True)
    email = models.EmailField('电子邮件',max_length=64,null=True)

    def __str__(self):
        return self.username

    class Meta():
        verbose_name='用户表'
        verbose_name_plural=verbose_name
        db_table='userprofile'

#成绩表
class Grade(models.Model):
    sid=models.ForeignKey(verbose_name='学生',to=UserProfile,on_delete=models.CASCADE,default='')
    subject=models.ForeignKey(verbose_name='科目',to="teacher.Paper",on_delete=models.CASCADE)
    grade=models.IntegerField(verbose_name='成绩')

    def __str__(self):
        return self.sid.username

    class Meta():
        verbose_name = '成绩表'
        verbose_name_plural = verbose_name
        db_table = 'grade'




















