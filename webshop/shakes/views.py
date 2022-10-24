from django.shortcuts import render
from .models import shakes

# Create your views here.

def shakes(request):
    shakes = shakes.objects.all().order_by('name')
    return render(request, 'shakes.html', {'shakes': shakes})
