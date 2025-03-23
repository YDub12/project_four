from django.urls import path
from .views import home, menu, reservations, contact

urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('reservations/', reservations, name='reservations'),
    path('contact/', contact, name='contact'),
]