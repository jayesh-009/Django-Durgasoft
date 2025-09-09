from django.contrib import admin
from AugustApp.models import Employee,Student,Stud,Movie

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']


admin.site.register(Employee,EmployeeAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display=['name','marks']
    
admin.site.register(Student,StudentAdmin)

class StudAdmin(admin.ModelAdmin):
    list_display=['name','marks']
    
admin.site.register(Stud,StudAdmin)

class MovieAdmin(admin.ModelAdmin):

    list_display=['rdate','moviename','hero','heroine','rating']


admin.site.register(Movie,MovieAdmin)
