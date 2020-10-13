from django import forms

#信息表单
class InfoForm(forms.Form):
    name=forms.CharField(label='姓名',max_length=32)
    text=forms.CharField(label='输入框')