from django import forms
from .models import Reservation, Table, Contact
import datetime
from django.core.exceptions import ValidationError

class ReservationForm(forms.ModelForm):
    reservation_time = forms.ChoiceField(
        choices=[],
        widget = forms.Select(attrs={'class': 'form-select'}),
        label="Time"
    )
    
    guest_count = forms.IntegerField(
        min_value=1,
        max_value=20,
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label="Number of Guests"
    )

    class Meta:
        model = Reservation
        fields = ['name','table', 'reservation_date', 'reservation_time', 'guest_count', 'status']
        widgets = {
            'reservation_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the logged-in user
        super().__init__(*args, **kwargs)

        if user:
                tables = Table.objects.filter(restaurant__id=1)
                self.fields['table'].queryset = tables

                self.fields['table'].label_from_instance = lambda obj: f"Table {obj.table_number} ({obj.capacity} seats)"

        date = self.data.get('reservation_date') or self.initial.get('reservation_date')
        table_id = self.data.get('table') or self.initial.get('table')

        self.fields['reservation_time'].choices = self.generate_time_slots(date, table_id)
    
    def generate_time_slots(self, reservation_date, table_id):
        start = datetime.time(12, 0)
        end = datetime.time(22, 0)
        step = datetime.timedelta(minutes=15)

        # If no date/table selected, return all slots
        if not reservation_date or not table_id:
            return self.full_day_slots(start, end, step)

        booked_times = Reservation.objects.filter(
            table_id=table_id,
            reservation_date=reservation_date
        ).values_list('reservation_time', flat=True)

        blocked = set()
        for time in booked_times:
            time_dt = datetime.datetime.combine(datetime.date.today(), time)
            for i in range(0, 6):  # Block 90 mins = 6 x 15min
                blocked_time = (time_dt + datetime.timedelta(minutes=15 * i)).time()
                blocked.add(blocked_time)

        slots = []

        current = datetime.datetime.combine(datetime.date.today(), start)
        end_dt = datetime.datetime.combine(datetime.date.today(), end)

        while current <= end_dt:
            time_only = current.time()
            time_str = time_only.strftime('%H:%M')
            if time_only not in blocked:
                slots.append((time_str, time_str))
            current += step

        return slots 
    
    def full_day_slots(self, start, end, step):
        slots = []
        current = datetime.datetime.combine(datetime.date.today(), start)
        end_dt = datetime.datetime.combine(datetime.date.today(), end)

        while current <= end_dt:
            time_only = current.time()
            time_str = time_only.strftime('%H:%M')
            slots.append((time_str, time_str))
            current += step

        return slots
    
    def clean(self):
        cleaned_data = super().clean()
        table = cleaned_data.get('table')
        reservation_date = cleaned_data.get('reservation_date')
        reservation_time_str = cleaned_data.get('reservation_time')

        if not (table and reservation_date and reservation_time_str):
            return cleaned_data

        try:
            reservation_time = datetime.datetime.strptime(reservation_time_str, '%H:%M').time()
        except (TypeError, ValueError):
            raise ValidationError("Invalid reservation time format.")

        reservation_start = datetime.datetime.combine(reservation_date, reservation_time)
        reservation_end = reservation_start + datetime.timedelta(minutes=90)

        existing_reservations = Reservation.objects.filter(
            table=table,
            reservation_date=reservation_date
        )

        for existing in existing_reservations:
            existing_start = datetime.datetime.combine(existing.reservation_date, existing.reservation_time)
            existing_end = existing_start + datetime.timedelta(minutes=90)

            if reservation_start < existing_end and reservation_end > existing_start:
                raise ValidationError("This table is already booked during the selected time.")

        return cleaned_data
    
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }