from django.shortcuts import render
from django.http import HttpResponse


def index3(request):
    return HttpResponse("<html><body><h1>Hello! You are in app 'TAG'</h1></body></html>")