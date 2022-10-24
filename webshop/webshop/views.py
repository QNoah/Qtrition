from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Home!')
    return render(request, 'index.html')

def shakes(request):
    # return HttpResponse('About!')
    return render(request, 'shakes.html')