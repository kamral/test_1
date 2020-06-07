from django.shortcuts import render
from .models import CustomUser
from .forms import (
    CustomUserCreationForm
)
from django.views.generic import CreateView
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url =reverse_lazy('login')
    template_name = 'signup.html'

