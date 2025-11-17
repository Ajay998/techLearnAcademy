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

class TrainerAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'expertise', 'trainer_photo']
    list_filter = ['expertise']
    search_fields = ['first_name', 'last_name', 'email']
    list_editable = ['expertise']
    list_display_links = ['full_name', 'email']
    ordering = ['-id']


admin.site.register(Course,CourseAdmin)
admin.site.register(Trainer,TrainerAdmin)
