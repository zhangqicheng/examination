from django.contrib import admin
from app01 import models
# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.Grade)
admin.site.register(models.Institute)
admin.site.register(models.Profession)
