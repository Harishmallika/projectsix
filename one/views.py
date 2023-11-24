from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def book1(request):
    return render(request,'book1.html')


def abd(request):
    return HttpResponse('<h1> hello welcome </h1>')
