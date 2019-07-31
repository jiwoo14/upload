from django.shortcuts import render
from .models import Hello

# Create your views here.

def home(request):
    hello = Hello.objects
    return render(request, 'home.html', {'upload': hello})