from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def firstlook(request):
    return HttpResponse("this is my app's first look.")
