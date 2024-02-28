
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm, ProfileForm
from django.contrib.auth import logout
from .models import UserProfile as UP
from django.contrib.auth.decorators import login_required

def logout_view(request):
    logout(request)
    return redirect('user_login')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_profile')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'User/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_profile')  
    else:
        form = CustomAuthenticationForm()
    return render(request, 'User/login.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid:
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
    else:
        form = ProfileForm()
    
    prof = None
    if UP.objects.filter(user=request.user).exists():
        prof = UP.objects.get(user=request.user)
    
    return render(request, 'User/profile.html', {'form':form, 'profile':prof})