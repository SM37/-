from django.shortcuts import render

# Create your views here.

# gifts/views.py
from django.shortcuts import render

def gift_list(request):
    return render(request, 'gifts/list.html')