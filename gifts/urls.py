from . import views
from django.urls import path, include

# gifts/urls.py
app_name = 'gifts'
urlpatterns = [
    path('', views.gift_list, name='list'),
]