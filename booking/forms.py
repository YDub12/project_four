from django import forms
from .models import Reservation, Table

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table', 'reservation_date', 'reservation_time', 'status']
        widgets = {
            'reservation_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'reservation_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the logged-in user
        super().__init__(*args, **kwargs)
        if user:
            self.fields['table'].queryset = Table.objects.filter(restaurant__id=1)