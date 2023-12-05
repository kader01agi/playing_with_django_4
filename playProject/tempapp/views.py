from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def read(request):
    return render(request, 'blog/read.html')

def about(request):
    return render(request, 'blog/about.html')

def contacts(request):
    return render(request, 'blog/contacts.html')
