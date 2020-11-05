from django import forms
from app01 import models as app_models

# class Base(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(Base, self).__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs.update({'class': 'form-control'})

#信息表单
class InfoForm(forms.ModelForm):
    username = forms.CharField(max_length=12,widget=forms.TextInput,label='用户名')
    class Meta:
        model=app_models.UserProfile
        fields=['id','username','password','sex','academy','profession','birth','email']
        exclude=['roles','academy','password']
        error_messages={
            'username':{
                'required':'姓名不能为空',
                'max_length':'长度不能超过13个中文字符，特殊除外',
                'invalid': '邮箱格式错误..',
            },
            'id': {
                'required': '学号或工号不能为空',
                'max_length': '长度不能超过13个中文字符，特殊除外',
                'invalid': '格式错误..',
            },
            'password': {
                'required': '密码不能为空',
                'max_length': '长度不能超过13个中文字符，特殊除外',
                'invalid': '邮箱格式错误..',
            },
            'birth': {
                'required': '出生日期不能为空',
                'max_length': '长度不能超过13个中文字符，特殊除外',
                'invalid': '邮箱格式错误..',
            },
            'email': {
                'required': '邮箱不能为空',
                'max_length': '长度不能超过13个中文字符，特殊除外',
                'invalid': '邮箱格式错误..',
            },
        },
    def __init__(self, *args, **kwargs):
        super(InfoForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})