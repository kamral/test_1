from django.urls import path
from .views import TodoAPIView,DetailAPIView

urlpatterns=[
    path('<int:pk>/', DetailAPIView.as_view()),
    path('', TodoAPIView.as_view()),
]