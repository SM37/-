from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'home.html')

@login_required
def my_requests(request):
    return render(request, 'my_requests.html')

@login_required
def create_request(request):
    return render(request, 'create_request.html')

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # или укажи другую нужную страницу
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})