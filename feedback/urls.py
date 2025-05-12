from . import views
from django.urls import path, include

# gifts/urls.py
app_name = 'feedback'
urlpatterns = [
    path('', views.gift_form, name='form'),
]