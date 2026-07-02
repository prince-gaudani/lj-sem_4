from django.shortcuts import render,redirect
from .models import Player

# Create your views here.
def home(request):
    search=request.GET.get('search')
    if search:
        players=Player.objects.filter(name__icontains=search)
    else:
        players=Player.objects.all()
    return render(request,'home.html',{'players':players})

def add_player(request):
    if request.method=="POST":
        Player.objects.create(
            Name=request.POST['name'],
            Test_Innings=request.POST['innings'],
            Runs=request.POST['runs'],
        )
        return redirect('home')
    return render(request,'add_player.html')

def edit_player(request,id):
    player=Player.objects.get(id=id)
    if request.method=='POST':
        player.Name=request.POST['name']
        player.Test_Innings=request.POST['innings']
        player.Runs=request.POST['runs']
        player.save()
        return redirect('home')
    return render(request,'edit_player.html',{'player':player})

