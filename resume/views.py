from django.shortcuts import render
from django.http import HttpResponse
from .models import Experience

def index(request):
    experience = Experience.objects.all()
    return render(request, 'index.html', {'experience': experience})

def test(request):
    return HttpResponse("<h1>tesе page</h1>")
