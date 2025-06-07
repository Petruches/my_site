from django.shortcuts import render
from django.http import HttpResponse
from .models import Experience, Me


def index(request):
    experience = Experience.objects.all()
    return render(request, 'index.html', {'experience': experience})


def me(request):
    me = Me.objects.all()
    return render(request, 'me/_me.html', {'me': me})


def content(request):
    return render(request, 'content/_content.html')
