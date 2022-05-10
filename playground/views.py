from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# MongoDB Connection
import pymongo
from pymongo import MongoClient
from credentials import secrets

db_user = secrets.get('DATABASE_USER', 'root')
db_pass = secrets.get('DATABASE_PASSWORD', 'pass')
print('user: ', db_user)
print('pass: ', db_pass)

cluster = MongoClient(f'mongodb+srv://{db_user}:{db_pass}@robonatty-cluster.cykzb.mongodb.net/Store?retryWrites=true&w=majority')
db = cluster["Store"]
collection = db["Products"]

blackMug = {"_id": 0, "name": "Mug", "description": "A mug with logo", "price": 10.00, "quantity": 10, "_categoryid": 0, "size": "One-Size", "color": "Black", "productAvailable": True, "sizeAvailable": True, "colorAvailable": True}
whiteMug = {"_id": 1, "name": "Mug", "description": "A mug with logo", "price": 10.00, "quantity": 7, "_categoryid": 0, "size": "One-Size", "color": "White", "productAvailable": True, "sizeAvailable": True, "colorAvailable": True}
collection.insert_many([whiteMug, blackMug])


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