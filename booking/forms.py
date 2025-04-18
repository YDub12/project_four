from django import forms
from .models import Reservation, Table
import datetime

class ReservationForm(forms.ModelForm):
    reservation_time = forms.ChoiceField(
        choices=[],
        widget = forms.Select(attrs={'class': 'form-select'}),
        label="Time"
    )
    class Meta:
        model = Reservation
        fields = ['table', 'reservation_date', 'reservation_time', 'status']
        widgets = {
            'reservation_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the logged-in user
        super().__init__(*args, **kwargs)

        if user:
            self.fields['table'].queryset = Table.objects.filter(restaurant__id=1)

        self.fields['reservation_time'].choices = self.generate_time_slots()
    
    def generate_time_slots(self):
        start = datetime.time(12, 0)
        end = datetime.time(22, 0)
        step = datetime.timedelta(minutes=15)

        current = datetime.datetime.combine(datetime.date.today(), start)
        end_dt = datetime.datetime.combine(datetime.date.today(), end)

        times = []
        while current <= end_dt:
            time_str = current.time().strftime('%H:%M')
            times.append((time_str, time_str))
            current += step

        return times