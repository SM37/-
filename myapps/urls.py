# myapps/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # домашняя страница
    path('my-requests/', views.my_requests, name='my_requests'),
    path('create-request/', views.create_request, name='create_request'),
    path('register/', views.register, name='register'),
]