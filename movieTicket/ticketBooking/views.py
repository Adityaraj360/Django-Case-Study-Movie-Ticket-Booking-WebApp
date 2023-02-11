from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# from ticketBooking.models import SignUp
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
import json
from django.core import serializers
# from .forms import LoginForm

# Create your views here.
from django.contrib.auth.decorators import login_required


def seats(request):
    all_seats=Seats.objects.all()
    return render(request,"seats.html",{'all_seats':all_seats})

def bookings(request,para):
    dict=json.loads(para)
    for i in range(len(dict['Seats'])):
        dict['Seats'][i]+=1
        if(dict['Seats'][i]<=8):
            f=Seats.objects.filter(S_no1=dict['Seats'][i])
            f.update(Status1="Booked")
        elif(dict['Seats'][i]<=16):
            f=Seats.objects.filter(S_no2=dict['Seats'][i])
            f.update(Status2="Booked")
        elif(dict['Seats'][i]<=24):
            f=Seats.objects.filter(S_no3=dict['Seats'][i])
            f.update(Status3="Booked")
        elif(dict['Seats'][i]<=32):
            f=Seats.objects.filter(S_no4=dict['Seats'][i])
            f.update(Status4="Booked")
        elif(dict['Seats'][i]<=40):
           f= Seats.objects.filter(S_no5=dict['Seats'][i])
           f.update(Status5="Booked")
        elif(dict['Seats'][i]<=48):
           f=Seats.objects.filter(S_no6=dict['Seats'][i])
           f.update(Status6="Booked")
    Bookings_list = Bookings.objects.all()       
    temp=Bookings(movie_name=dict['movie'],selected_seats=dict['Seats'],price=dict['price'])
    temp.save()
    return render(request,"bookings.html",{'bookings_list' : Bookings_list})

def signup(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('login')
    context = {'form':form}
    print(context)
    return render(request, 'signup.html',context) 

def loginUser(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            return redirect('signup')

    else:
        form = AuthenticationForm(request, data = request.POST)
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def movieAdd(request):
    if request.method == "POST":
        name = request.POST['movieName']
        image = request.POST['image']
        date = request.POST['date']
        duration = request.POST['duration']
        movietype = request.POST['movietype']
        language = request.POST['language']
        rating = request.POST['rating']
        trailer = request.POST['trailer']
        price = request.POST['price']
        print([name, str(date), duration,movietype,language,rating,trailer,price])
        temp = Movies(name = name, image = image, date = date, duration = duration, type = movietype, language = language, rating = rating, trailer = trailer, price = price)
        temp.save()
        print("Data added")
        return redirect('home')
    return render(request, 'index.html') 



@login_required(login_url='login')
def movieList(request):
    movies_list = Movies.objects.all()
    # print(movies_list[1])
    return render(request, 'moviesList.html', {'movies_list' : movies_list})

@login_required(login_url='login')
def movieDelete(request,pk):
    movie = Movies.objects.get(id=pk)
    movie.delete()  
    return redirect('movieList')
