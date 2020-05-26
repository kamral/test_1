from django.urls import path
from . import views

urlpattenrs=[
    path('', views.HomePageView, name='home')
]