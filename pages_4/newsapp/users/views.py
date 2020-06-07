from django.shortcuts import render
from .models import CustomUser
from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
)
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'home.html'