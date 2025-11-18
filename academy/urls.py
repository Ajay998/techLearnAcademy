from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('academy/course/', views.course,name='course'),
    path('academy/trainer/', views.trainer, name='trainer'),
    path('academy/student/', views.student, name='student'),
]
