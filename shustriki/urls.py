from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/', include('accounts.urls')),
    path('survey/', include('survey.urls')),
    path('gifts/', include('gifts.urls')),
    path('feedback/', include('feedback.urls')),
    path('myapps/', include('myapps.urls')),
]