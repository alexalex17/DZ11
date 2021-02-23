from django.shortcuts import render
from django.http import HttpResponse


def index2(request):
    return HttpResponse("<html><body><h1>Hello! You are in app 'POST'</h1></body></html>")