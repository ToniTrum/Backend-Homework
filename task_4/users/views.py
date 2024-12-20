from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import User
from .forms import UserLoginForm, UserRegisterForm

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserLoginForm()
    context = {
        "form": form
    }
    return render(request, 'login.html', context)

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Успешная регистрация!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('users:index'))

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})
