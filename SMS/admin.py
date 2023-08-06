from django.contrib import admin
from SMS.models import *
#admin.site.register(Student)

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','age','address']
