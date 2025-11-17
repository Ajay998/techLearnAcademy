from django.contrib import admin
from . models import *
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ["id","course_name","description","duration","course_image"]
    list_filter = ["course_name"]
    search_fields = ['course_name']
    list_editable = ["duration"]
    list_display_links = ["course_name"]
    ordering = ["-id"]


admin.site.register(Course,CourseAdmin)
