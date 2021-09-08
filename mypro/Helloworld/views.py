from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Hello(Request):
    return HttpResponse('<h1>Hello World!</h>')

def Homepage(request):
    return render(request,'home.html')
