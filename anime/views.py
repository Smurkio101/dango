from django.http import HttpResponse
from django.shortcuts import render


def anime(request): 
    return render(request, 'anime/anime.html',{'anime': ['anime1', 'anime2']}) 

def home(request): 
    return HttpResponse("home page")
