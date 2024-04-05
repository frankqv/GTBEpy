from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def erro404(request):
    return render(request, 'erro404.html')
def erro500(request):
    return render(request, 'erro500.html')
def login(request):
    return render(request, 'frontend/login.html')
def registrar(request):
    return render(request, 'registrar.html')