from django.urls import path
from . import views

app_name = 'IMPS_App'

urlpatterns = [
    path('', views.Lobby_view, name='lobby'),  # Homepage
    path('admin_dashboard/', views.admin_dashboard_view, name='admin_dashboard'),  # Admin
    path('student_dashboard/', views.student_dashboard_view, name='student_dashboard'),  # Student
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]
