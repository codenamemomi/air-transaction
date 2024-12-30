from django.urls import path
from .import views  
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/', views.login_page, name= 'login'),
    path('', views.get_account_summary, name= 'home'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]