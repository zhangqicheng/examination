from django.contrib import admin
from app01 import models
# Register your models here.
admin.site.register(models.Student)
admin.site.register(models.Teacher)
admin.site.register(models.QuestionSingle)
admin.site.register(models.Grade)
admin.site.register(models.Paper)
admin.site.register(models.Institute)
admin.site.register(models.Profession)
