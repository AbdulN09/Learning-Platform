from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'Home.html')

def python(request):
    return render(request,'python.html')


def java(request):
    return render(request,'java.html')


def mern(request):
    return render(request,'mern.html')

def pythonnotes(request):
    return render(request,'python_notes.html')

def javanotes(request):
    return render(request,'java notes.html')


def mernnotes(request):
    return render(request,'mern notes.html')