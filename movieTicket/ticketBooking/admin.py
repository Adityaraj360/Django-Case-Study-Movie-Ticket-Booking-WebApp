from django.contrib import admin
# from ticketBooking.models import SignUp
from .models import Movies, Bookings,Seats,shows
# Register your models here.

# admin.site.register(SignUp)

admin.site.register(Movies)
admin.site.register(Bookings)
admin.site.register(Seats)
admin.site.register(shows)
