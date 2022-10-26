from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    shake = shakes.objects.all()
    return render(request, 'shakes.html', {'shakes': shake})
