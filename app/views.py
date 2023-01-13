from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hai(request,name):
    return HttpResponse(f' welocome to hai{name}')