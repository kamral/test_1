from django.urls import path
from .views import  (
    BLogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

urlpatterns=[
    path('post/new/', BlogCreateView.as_view(),
         name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(),
         name='post_detail'),
    path('post/<int:pk>/update/', BlogUpdateView.as_view(),
         name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(),
         name='post_delete'),
    path('',BLogListView.as_view(),
         name='home'),
]