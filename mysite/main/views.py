from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return redirect('home')

def home(request):
    return render(request, 'home.html')

def login(request):
    return HttpResponse('<h1>Login Page</h1>')

def signup(request):
    return HttpResponse('<h1>SignUp Page</h1>')