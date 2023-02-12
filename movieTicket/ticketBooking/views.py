from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from ticketBooking.models import SignUp
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
import json
from django.contrib.auth.models import User
# from .forms import LoginForm

# Create your views here.
from django.contrib.auth.decorators import login_required


def seats(request,pk,time):
    movie = Movies.objects.get(id=pk)
    all_seats= Seats.objects.filter(From_time=time)
    return render(request,"seats.html", {'movie' : movie, 'all_seats':all_seats, 'time':time})

def bookings(request,para,pk):
    dict=json.loads(para)
    for i in range(len(dict['Seats'])):
        dict['Seats'][i]=int(dict['Seats'][i])
        if(dict['Seats'][i]<=7):
            f=Seats.objects.filter(S_no1=dict['Seats'][i],From_time=dict['time'])
            f.update(Status1="Booked")
        elif(dict['Seats'][i]<=15):
            f=Seats.objects.filter(S_no2=dict['Seats'][i],From_time=dict['time'])
            f.update(Status2="Booked")
        elif(dict['Seats'][i]<=23):
            f=Seats.objects.filter(S_no3=dict['Seats'][i],From_time=dict['time'])
            f.update(Status3="Booked")
        elif(dict['Seats'][i]<=31):
            f=Seats.objects.filter(S_no4=dict['Seats'][i],From_time=dict['time'])
            f.update(Status4="Booked")
        elif(dict['Seats'][i]<=39):
           f= Seats.objects.filter(S_no5=dict['Seats'][i],From_time=dict['time'])
           f.update(Status5="Booked")
        elif(dict['Seats'][i]<=47):
           f=Seats.objects.filter(S_no6=dict['Seats'][i],From_time=dict['time'])
           f.update(Status6="Booked")      
    temp=Bookings(movie_name=dict['movie'],selected_seats=dict['Seats'],price=int(dict['price']),u_name=request.user.get_username(),Show_time=dict['time'])
    print(temp)
    temp.save()
    Bookings_list = Bookings.objects.filter(u_name=request.user.get_username())
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
    admin_username = "admin12345"
    admin_password = "Newuser@12345"
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            if admin_username == username and admin_password == password:
                # print("Admin")
                # print({admin_username : username, admin_password : password})
                login(request, user)
                return redirect('movieAdd')
            else:
                print("Non Admin")
                print({admin_username : username, admin_password : password})

            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'username or password not correct')
            return redirect('login')

    else:
        form = AuthenticationForm(request, data = request.POST)
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    movies_list = Movies.objects.all()
    return render(request, 'home.html', {'movies_list' : movies_list})

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
        return redirect('movieList')
    return render(request, 'movieAdd.html') 



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

@login_required(login_url='login')
def details(request, pk):
    movie = Movies.objects.get(id=pk)
    Shows= shows.objects.filter(M_id=pk)
    return render(request, 'details.html', {'movie' : movie, 'Shows':Shows})

def adHome(request):
    return render(request, 'adHome.html')
