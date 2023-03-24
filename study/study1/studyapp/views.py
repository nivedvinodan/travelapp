from django.http import HttpResponse
from django.shortcuts import render

from .models import Place, Person


# Create your views here.
def study(request):
    obj = Place.objects.all()
    objs = Person.objects.all()
    return render(request, "index.html", {'result': obj, 'results': objs})

# def addition(request):
#     x=int(request.GET['num1'])
#     y =int (request.GET['num2'])
#     add=x+y
#     sub=x-y
#     mult=x*y
#     div=x/y
#     return render(request,"addition.html",{'add':add,'sub':sub,'mult':mult,'div':div})
