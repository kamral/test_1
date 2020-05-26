from django.urls import path
from .views import SignUpView

urlpattterns=[
    path('signup/', SignUpView.as_view(), name='signup'),

]