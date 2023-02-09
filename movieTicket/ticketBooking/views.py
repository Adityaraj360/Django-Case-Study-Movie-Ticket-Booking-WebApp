from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# from ticketBooking.models import SignUp
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
# from .forms import LoginForm

# Create your views here.


def signup(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('contact')
    context = {'form':form}
    print(context)
    return render(request, 'signup.html',context) 

def contact(request):
    return render(request, 'trial.html')

def loginUser(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('contact')
        else:
            return redirect('signup')

    else:
        form = AuthenticationForm(request, data = request.POST)
    return render(request, 'login.html')