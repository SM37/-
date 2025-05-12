from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm  # Импортируем CustomUserCreationForm

# Главная страница
def home(request):
    return render(request, 'home.html')


# Страница "Мои запросы" (доступ только для авторизованных пользователей)
@login_required
def my_requests(request):
    return render(request, 'my_requests.html')


# Страница создания запроса (доступ только для авторизованных пользователей)
@login_required
def create_request(request):
    return render(request, 'create_request.html')

# Регистрация нового пользователя
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Используем CustomUserCreationForm
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Добро пожаловать, {user.username}!')
            return redirect('home')  # Перенаправление на главную страницу
        else:
            # Если форма не прошла валидацию, покажем ошибки пользователю
            messages.error(request, 'Ошибка при регистрации. Пожалуйста, проверьте форму.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})