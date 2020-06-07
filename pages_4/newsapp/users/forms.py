from django import forms
from .models import CustomUser
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm
)
from django.urls import reverse_lazy


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=CustomUser
        fields = UserCreationForm.Meta.fields

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = UserChangeForm.Meta.fields


