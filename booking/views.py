from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Reservation
from .forms import ReservationForm, ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'booking/home.html')

def menu(request):
    return render(request, 'booking/menu.html')

def booking(request):
    return render(request, "booking/booking.html")

def booking(request):
    if request.method == "POST":
        form = ReservationForm(request.POST, user=request.user)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user  # Assign logged-in user
            reservation.status = 'pending'  # Default status
            reservation.save()
            return redirect('booking_success')  # Redirect to success page
    else:
        form = ReservationForm(user=request.user)

    return render(request, "booking/booking.html", {"form": form})

def booking_success(request):
    return render(request, "booking/booking_success.html")

def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        contact = form.save()  # Save to database

        # Send email to restaurant/admin
        send_mail(
            subject=f"New Contact Message: {contact.subject}",
            message=f"From: {contact.name} <{contact.email}>\n\n{contact.message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=["gozj3ybw@students.codeinstitute.net"],  
        )

        messages.success(request, "Thanks for reaching out! We will be in touch.")
        return redirect('contact')

    return render(request, 'booking/contact.html', {
        'form': form,
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY,
    })

def get_available_times(request):
    table_id = request.GET.get('table_id')
    date = request.GET.get('reservation_date')

    if not table_id or not date:
        return JsonResponse({'times': []})

    form = ReservationForm()
    time_choices = form.generate_time_slots(date, table_id)
    times = [time for time, label in time_choices]

    return JsonResponse({'times': times})

@login_required
def dashboard(request):
    reservations = Reservation.objects.filter(user=request.user).order_by('reservation_date', 'reservation_time')
    return render(request, 'booking/dashboard.html', {'reservations': reservations})