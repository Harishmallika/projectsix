from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def abd(request):
    return render(request,'hp.html')




def sivakumar(request):
    return HttpResponse('<h1> ah hi </h1>')
