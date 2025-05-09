from django.contrib.auth import views as auth_views
from django.urls import path, include  # добавьте include

urlpatterns = [
    path('', include('myapps.urls')),  # подключаем urls из myapps
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]