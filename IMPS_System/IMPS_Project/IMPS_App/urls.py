from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

# Rest of your code...

app_name = 'IMPS_App'

urlpatterns = [
    path('', views.Lobby_view, name='lobby'),  # Homepage
    path('admin_dashboard/', views.admin_dashboard_view, name='admin_dashboard'),  # Admin
    path('student_dashboard/', views.student_dashboard_view, name='student_dashboard'),  # Student
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
