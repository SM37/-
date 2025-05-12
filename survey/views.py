# Create your views here.

from django.shortcuts import render
from .forms import SurveyForm

def survey_form(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'survey/success.html')
    else:
        form = SurveyForm()
    return render(request, 'survey/form.html', {'form': form})