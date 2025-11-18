from django.shortcuts import render
from .models import Course, Trainer, Student
# Create your views here.

def home(request):
    total_course = Course.objects.all().count()
    total_trainer = Trainer.objects.all().count()
    total_student = Student.objects.all().count()
    context = {
        "total_course" : total_course,
        "total_trainer" : total_trainer,
        "total_student" : total_student
    }
    return render(request,"homePage.html",context)

def course(request):
    courses = Course.objects.all()
    context = {
        "courses" :  courses
    }
    return render(request,"coursePage.html",context)

def trainer(request):
    trainers = Trainer.objects.all()
    context = {
        "trainers" :  trainers
    }
    return render(request,"trainerPage.html",context)

def student(request):
    students = Student.objects.all()
    context = {
        "students" :  students
    }
    return render(request,"studentPage.html",context)

