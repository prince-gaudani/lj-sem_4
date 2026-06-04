from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def details(request):
    return HttpResponse("<h1>XYZ Roll no 135 Division D5</h1>")
