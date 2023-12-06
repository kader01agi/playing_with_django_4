from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('read/', views.read),
    path('about/', views.about),
    path('contacts/', views.contacts),

]
