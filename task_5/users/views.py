from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import User
from .forms import UserLoginForm, UserRegisterForm, UserUpdateForm

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

@login_required
def update(request):
    if request.method == "POST":
        form = UserUpdateForm(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            new_password = form.cleaned_data.get('password')
            if new_password:
                user.set_password(new_password)
            user.save()
            messages.success(request, 'Успешное изменение!')
            auth.update_session_auth_hash(request, user)
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserUpdateForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'update.html', context)

@login_required
def delete(request):
    user = request.user
    user.delete()
    return HttpResponseRedirect(reverse('users:index'))
