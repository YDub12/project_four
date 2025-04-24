from django.urls import path
from .views import home, menu, booking, contact, booking_success
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('booking/', booking, name='booking'),
    path('contact/', contact, name='contact'),
    path('booking/success/', booking_success, name='booking_success'),
    path('get-available-times/', views.get_available_times, name='get_available_times'),
]