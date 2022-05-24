from unicodedata import name
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from pymongo import MongoClient
from store.credentials import secrets

# MongoDB Connection

db_user = secrets.get('DATABASE_USER', 'root')
db_pass = secrets.get('DATABASE_PASSWORD', 'pass')

cluster = MongoClient(f'mongodb+srv://{db_user}:{db_pass}@robonatty-cluster.cykzb.mongodb.net/Store?retryWrites=true&w=majority')

mydb =  cluster["Store"] 
mycol =  mydb["Category"]



# Product Related
def index(request):
    return render(request, "index.html", {"name": "Alexa"})

def products(request):
    if request.method == "GET":
        return render(request, "product_routes/categories.html", category)

def category(request, category):
    if request.method == "GET":
        category = mycol.find_one()
        print(category)
        return render(request, "product_routes/category.html", {"category" : category})

def product(request, category, id):
    if request.method == "GET":
        return render(request, "product_routes/product.html", {"category" : category, "id": id})