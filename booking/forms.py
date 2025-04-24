from django import forms
from .models import Reservation, Table, Contact
import datetime

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
            self.fields['table'].queryset = Table.objects.filter(restaurant__id=1)

        date = self.data.get('reservation_date') or self.initial.get('reservation_date')
        table_id = self.data.get('table') or self.initial.get('table')

        self.fields['reservation_time'].choices = self.generate_time_slots(date, table_id)
    
    def generate_time_slots(self, reservation_date, table_id):
        start = datetime.time(12, 0)
        end = datetime.time(22, 0)
        step = datetime.timedelta(minutes=15)

        # Default to all slots if no date/table selected yet
        if not reservation_date or not table_id:
            return self.full_day_slots(start, end, step)

        # Get all booked times for that table on the selected date
        booked_times = Reservation.objects.filter(
            table_id=table_id,
            reservation_date=reservation_date
        ).values_list('reservation_time', flat=True)

            # Build list of 1-hour blocked slots
        blocked = set()
        for time in booked:
            time_dt = datetime.datetime.combine(datetime.date.today(), time)
            # Block 1 hour range (15 mins before and 45 after)
            for i in range(-1, 4):  # 5 slots: -15, 0, +15, +30, +45
                blocked_time = (time_dt + datetime.timedelta(minutes=15 * i)).time()
                blocked.add(blocked_time)

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