from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return redirect('/home/')

def home(request):
    return render(request, 'main/home.html')

def login(request):
    return render(request, 'main/login.html')

def signup(request):
    return render(request, 'main/signup.html')