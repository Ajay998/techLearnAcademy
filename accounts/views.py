from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib import auth

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        form = AuthenticationForm(request , data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return redirect('course')
        else:
            messages.error(request, 'Login failed. Please correct the errors below.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')