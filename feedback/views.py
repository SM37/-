# Create your views here.

# gifts/views.py

from django.shortcuts import render, redirect
from django import forms

def gift_form(request):
    # ваша логика
    return render(request, 'gifts/form.html')

from django.shortcuts import render, redirect
from django import forms
from .models import FeedbackMessage

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)

def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            FeedbackMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            return redirect('feedback:form')  # можно заменить на "спасибо" страницу
    else:
        form = FeedbackForm()
    return render(request, 'feedback/form.html', {'form': form})