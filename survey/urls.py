from django.urls import path
from . import views

app_name = 'survey'

urlpatterns = [
    path('create/', views.survey_form, name='create'),
]