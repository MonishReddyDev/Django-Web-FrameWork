from django.http import HttpResponse
from  django.shortcuts import render



def Home(request):
    return render(request,'index.html')

def start(request):
    return HttpResponse("This is from Home page")


def About(request):
    return HttpResponse("This is from About page")

