from django.shortcuts import render
from .models import Events

# Create your views here.
def home(request):
   return render(request,'home.html')

def events(request):
   allEvents=Events.objects.all()
   return render(request,"events.html",{'allEvents':allEvents})