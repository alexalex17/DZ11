from django.shortcuts import render
from django.http import HttpResponse


def index1(request):
    return HttpResponse("<html><body><h1>Hello! You are in app 'EDITOR'</h1></body></html>")