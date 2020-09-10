from django.http import HttpResponse
from django.shortcuts import render
from . import forms


def index(request):
    form = forms.TestForm()
    return render(request, 'index.html', {'form': form})
