from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm

#Register
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

#Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'login.html', {'form': form})
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

#Logout
def logout_view(request):
    logout(request)
    return redirect('login')
    
# Example view with user level check
@login_required  # Ensures only logged-in users can access this view
def dashboard_view(request):
    if request.user.profile.user_level == 'admin':
        # Code for admin users
        return render(request, 'admin_dashboard.html')
    elif request.user.profile.user_level == 'student':
        # Code for student users
        return render(request, 'student_dashboard.html')
    else:
        # Handle guests or other user levels
        return render(request, 'guest_dashboard.html')
