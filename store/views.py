from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Product Related
def index(request):
    return render(request, "index.html", {"name": "Alexa"})

def products(request):
    return render(request, "product_routes/categories.html")

def category(request, category):
    return render(request, "product_routes/category.html", {"category" : category})

def product(request, category, id):
    return render(request, "product_routes/product.html", {"category" : category, "id": id})