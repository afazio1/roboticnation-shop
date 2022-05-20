from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def say_hello(request):
    return render(request, "hello.html", {"name": "Alexa"})