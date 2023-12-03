from django.urls import path
from . import views


urlpatterns = [
    path('look/', views.firstlook)
]
