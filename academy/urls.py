from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('academy/course/', views.course,name='course'),
    path('academy/trainer/', views.trainer, name='trainer'),
    path('academy/student/', views.student, name='student'),

    path('academy/course/<int:id>',views.course_detail, name= "course_detail"),
    path('academy/course/edit/<int:id>',views.edit_course, name= "edit_course"),
    path('academy/course/delete/<int:id>',views.delete_course, name= "delete_course"),
]
