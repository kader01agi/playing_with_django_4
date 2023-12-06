from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    # return render(request, 'home.html')
    return render(request, 'tempapp/home.html')

def read(request):
    return render(request, 'tempapp/read.html')

def about(request):
    return render(request, 'tempapp/about.html')

def contacts(request):
    return render(request, 'tempapp/contacts.html')
