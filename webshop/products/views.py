from re import template
from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template = loader.get_template('products/products.html')
    return HttpResponse(template.render())