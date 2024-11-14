from django.urls import path
from . import views

app_name = 'IMPS_App'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('lobby/', views.dashboard_view, name='lobby'),
    path('admin_dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('student_dashboard/', views.student_dashboard_view, name='student_dashboard'),
    path('guest_dashboard/', views.guest_dashboard_view, name='guest_dashboard'),
]