from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'booking/home.html')

def menu(request):
    return render(request, 'booking/menu.html')

def reservations(request):
    return render(request, 'booking/reservations.html')

def contact(request):
    return render(request, 'booking/contact.html')

def contact(request):
    errors = []
    error_fields = []
    
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        # Validation
        if not name:
            errors.append("Name is required.")
            error_fields.append("name")
        if not email:
            errors.append("Email is required.")
            error_fields.append("email")
        elif "@" not in email or "." not in email:  # Basic email validation
            errors.append("Please enter a valid email address.")
            error_fields.append("email")
        if not message:
            errors.append("Message cannot be empty.")
            error_fields.append("message")

        # If no errors, send email
        if not errors:
            full_message = f"Message from {name} ({email}):\n\n{message}"
            send_mail(
                subject="New Contact Form Submission",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["yourrestaurant@example.com"],  # Change to your real email
            )
            return render(request, "booking/contact.html", {"success": True})

    return render(request, "booking/contact.html", {"errors": errors, "error_fields": error_fields})