from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def read(request):
    return render(request, 'read.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')
