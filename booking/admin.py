from django.contrib import admin
from .models import Restaurant, Table, Reservation, Contact

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(Reservation)
admin.site.register(Contact)