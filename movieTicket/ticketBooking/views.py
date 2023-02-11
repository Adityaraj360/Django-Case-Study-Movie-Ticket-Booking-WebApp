from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# from ticketBooking.models import SignUp
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
import json
# from .forms import LoginForm

# Create your views here.
from django.contrib.auth.decorators import login_required

def seats(request):
    return render(request,"seats.html")

def bookings(request,para):
    Bookings_list = Bookings.objects.all()
    dict=json.loads(para)
    temp=Bookings(movie_name=dict['movie'],selected_seats=dict['Seats'],prize=199)
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
            return redirect('signup')

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
    return render(request, 'details.html', {'movie' : movie})

def adHome(request):
    return render(request, 'adHome.html')
