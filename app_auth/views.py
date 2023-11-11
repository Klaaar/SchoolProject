from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.
@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    return render(request, 'app_auth/profile.html')
def login_view(request):
    redirect_url = reverse('profile')
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/login.html', {"error": "Пользователь не найден"})

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

def registration(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'app_auth/register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.set_password(form.cleaned_data['password1'])
            user.save()
            
            login(request, user)
            return redirect('posts')
        else:
            return render(request, 'app_auth/register.html', {'form': form})