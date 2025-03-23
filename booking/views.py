from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'booking/home.html')

def menu(request):
    return render(request, 'booking/menu.html')

def reservations(request):
    return render(request, 'booking/reservations.html')

def contact(request):
    return render(request, 'booking/contact.html')