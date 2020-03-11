from django.shortcuts import render
from .models import Portfolio

# Create your views here.
def home(request):
    projects = Portfolio.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})
