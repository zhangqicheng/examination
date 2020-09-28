from django.contrib import admin
from app01.models import Student,Teacher,QuestionSingle,Grade,Paper
# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(QuestionSingle)
admin.site.register(Grade)
admin.site.register(Paper)
