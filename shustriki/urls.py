from django.contrib import admin
from django.urls import path, include
from myapps import views as myapps_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('survey/', include('survey.urls')),
    path('gifts/', include(('gifts.urls', 'gifts'), namespace='gifts')),
    path('myapps/', include(('myapps.urls', 'myapps'), namespace='myapps')),
    path('feedback/', include(('feedback.urls', 'feedback'), namespace='feedback')),
]