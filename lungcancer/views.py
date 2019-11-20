from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'lungcancer/home.html')

def login(request):
    return render(request, 'lungcancer/login.html')

def register(request):
    return render(request, 'lungcancer/register.html')

def diagnosis(request):
    return render(request, 'lungcancer/diagnosis.html')

