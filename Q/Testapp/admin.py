from django.contrib import admin
from Testapp.models import Student

# Register your models here.
class StudentModelAdim(admin.ModelAdmin):
    list_display=['sno','sname','scity','semail']

admin.site.register(Student,StudentModelAdim)
