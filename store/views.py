from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request):
    return render(request, "index.html", {"name": "Alexa"})

def products(request):
    return render(request, "product_routes/products.html")

def product(request, id):
    return render(request, "product_routes/product.html", {"id": id})