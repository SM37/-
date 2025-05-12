# myapps/urls.py

from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('my_requests/', views.my_requests, name='my_requests'),
    path('create_request/', views.create_request, name='create_request'),
    path('register/', views.register, name='register'),
]

