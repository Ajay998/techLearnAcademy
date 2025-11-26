from django.shortcuts import render,get_object_or_404, redirect
from .models import Course, Trainer, Student
from .forms import CourseForm, TrainerForm, StudentForm
from django.contrib import messages

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
    return render(request,"course/coursePage.html",context)

def trainer(request):
    trainers = Trainer.objects.all()
    context = {
        "trainers" :  trainers
    }
    return render(request,"trainer/trainerPage.html",context)

def student(request):
    students = Student.objects.all()
    context = {
        "students" :  students
    }
    return render(request,"student/studentPage.html",context)

def course_detail(request, id):
    course_detail = get_object_or_404(Course, id=id)
    context = {
        "course_detail": course_detail
    }
    return render(request,"course/courseDetail.html", context)

def edit_course(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course updated successfully!')
            return redirect('course')
        else:
            messages.error(request, 'Update failed. Please check the form.')
    else:
        form = CourseForm(instance=course)
    return render(request, 'course/editCourse.html', {'course': course, 'form': form})

def delete_course(request, id):
    course = get_object_or_404(Course, id=id)
    course.delete()
    messages.success(request, 'Course deleted successfully!')
    return redirect('course')

def trainer_detail(request,id):
    trainer_detail = get_object_or_404(Trainer, id=id)
    context = {
        "trainer_detail": trainer_detail
    }
    return render(request,"trainer/trainerDetail.html", context)

def edit_trainer(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    if request.method == "POST":
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Trainer updated successfully!')
            return redirect('trainer')
        else:
            messages.error(request, 'Update failed. Please check the form.')
    else:
        form = TrainerForm(instance=trainer)
    return render(request, 'trainer/editTrainer.html', {'trainer': trainer, 'form': form})

def delete_trainer(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    trainer.delete()
    messages.success(request, 'Trainer deleted successfully!')
    return redirect('trainer')

def student_detail(request,id):
    student_detail = get_object_or_404(Student, id=id)
    context = {
        "student_detail": student_detail
    }
    return render(request,"student/studentDetail.html", context)

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('student')
        else:
            messages.error(request, 'Update failed. Please check the form.')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student/editStudent.html', {'student': student, 'form': form})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    messages.success(request, 'Student deleted successfully!')
    return redirect('student')