from django.contrib import admin
from fabi.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','stuid','stuname','stuemail','stuphone')
admin.site.register(Student, StudentAdmin)
# Register your models here.
