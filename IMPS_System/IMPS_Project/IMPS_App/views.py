from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

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
