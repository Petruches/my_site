from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # print(requex)
    #return HttpResponse('Hello world')
    return render(request, 'index.html')

def test(request):
    return HttpResponse("<h1>tesе page</h1>")
