from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse



def laptop(request):
    return render(request,'laptopdell.html')



def dell(request):
    return HttpResponse('<h1> boom boom  </h1>')