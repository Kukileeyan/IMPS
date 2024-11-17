from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm

# Register
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})

# Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                # Redirect based on user level
                user_level = getattr(user.profile, 'user_level', None)  # Safely access user_level
                if user_level == 'admin':
                    return redirect('admin_dashboard')
                elif user_level == 'student':
                    return redirect('student_dashboard')
                else:
                    return redirect('lobby')  # Default redirect

            else:
                return render(request, 'login.html', {'form': form})
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def admin_dashboard_view(request):
    if request.user.profile.user_level == 'admin':
        return redirect('admin_dashboard')      

def student_dashboard_view(request):
    if request.user.profile.user_level == 'student':
        return redirect('student_dashboard')

def Lobby_view(request):
    return render(request, 'Lobby.html')

