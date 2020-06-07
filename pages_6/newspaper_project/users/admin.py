from django.contrib import admin
from .models import CustomUser
# Register your models here.
from .forms import (
    CustomUserCreationForm,
    CutomUserChangeForm
)
from  django.contrib.auth.admin import UserAdmin

class CustomerAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CutomUserChangeForm
    model=CustomUser

admin.site.register(CustomUser, CustomerAdmin)