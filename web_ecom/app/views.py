from django.shortcuts import render # type: ignore
from django.http import HttpResponse # Create your views here

def home(request):
    return render(request, 'app/home.html')