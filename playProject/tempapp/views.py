from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'tempapp/home.html')

def read(request):
    name = "MD. ABDUL KADER"
    country = "Bangladesh"
    skills = ["Python", "Django", "HTML"]
    data = {"name": name, "country": country, "skills": skills}
    return render(request, 'tempapp/read.html', data)

def about(request):
    return render(request, 'tempapp/about.html')

def contacts(request):
    return render(request, 'tempapp/contacts.html')
