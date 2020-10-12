from django.db import models

# Create your models here.创建rbac权限组件
class Permission(models.Model):
    '''权限表'''
    title=models.CharField(verbose_name='标题',max_length=32)
    url=models.CharField(verbose_name='含有正则的url',max_length=128)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name='权限表'
        verbose_name_plural=verbose_name
        db_table='rbac_permission'

class Role(models.Model):
    '''角色表'''
    title=models.CharField(verbose_name='角色名称',max_length=32)
    permissions=models.ManyToManyField(verbose_name='拥有的权限',to=Permission)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name='角色表'
        verbose_name_plural=verbose_name
        db_table='rbac_role'

class UserInfo(models.Model):
    """
    用户表
    """
    name=models.CharField(verbose_name='用户名',max_length=32)
    password=models.CharField(verbose_name='密码',max_length=64)
    email=models.CharField(verbose_name='邮箱',max_length=32)
    roles=models.ManyToManyField(verbose_name='拥有的所有角色',to=Role,blank=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name='用户表'
        verbose_name_plural=verbose_name
        db_table='rbac_userinfo'
        abstract=True



