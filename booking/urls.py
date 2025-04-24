from django.urls import path
from .views import home, menu, booking, contact, dashboard, booking_success
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('booking/', booking, name='booking'),
    path('contact/', contact, name='contact'),
    path('booking/success/', booking_success, name='booking_success'),
    path('dashboard/', dashboard, name='dashboard'),
    path('get-available-times/', views.get_available_times, name='get_available_times'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]