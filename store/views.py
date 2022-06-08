from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# MongoDB Connection
from pymongo import MongoClient
# client = MongoClient('mongodb+srv://<username>:<password>@<atlas cluster>/<myFirstDatabase>?retryWrites=true&w=majority')
# db = client['shop']


# Product Related
def index(request):
    return render(request, "index.html", {"name": "Alexa"})

def products(request):
    if request.method == "GET":
        return render(request, "product_routes/categories.html")

def category(request, category):
    if request.method == "GET":
        return render(request, "product_routes/category.html", {"category" : category})

def product(request, category, id):
    if request.method == "GET":
        return render(request, "product_routes/product.html", {"category" : category, "id": id})

def cart(request):
    return render(request, "product_routes/cart.html")