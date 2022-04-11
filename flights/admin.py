from django.contrib import admin

from .models import Country,City,Airport,Flight,Booking,Passenger

# Register your models here.
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Booking)
admin.site.register(Passenger)