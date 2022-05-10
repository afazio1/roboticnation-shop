from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# MongoDB Connection
import pymongo
from pymongo import MongoClient
from credentials import user, pswd
# cluster = MongoClient('mongodb+srv://<user>:<pswd>@robonatty-cluster.cykzb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
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