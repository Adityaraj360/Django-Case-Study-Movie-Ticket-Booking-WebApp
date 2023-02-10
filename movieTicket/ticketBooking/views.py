from django.shortcuts import render
from django.http import HttpResponse
from ticketBooking.models import Person

# Create your views here.


def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        number = request.POST['number']
        print([username,email,password,number])
        temp = Person(username = username, password = password, email = email, mobile = number)
        temp.save()
        print("Data added")
    return render(request, 'index.html') 

def bookings(request):
    return render(request, 'bookings.html') 