from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'home.html')

def erro404(request):
    return render(request, 'frontend/erro404.html')

def erro500(request):
    return render(request, 'frontend/erro500.html')

def registrar(request):
    return render(request, 'frontend/registrar.html')

def escritorio(request):
    # Tu lógica aquí
    return render(request, 'frontend/escritorio.html')


def login(request):
    # Tu lógica aquí
    return render(request, 'frontend/login_view.html')