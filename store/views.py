import this
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from pymongo import MongoClient
from storefront.credentials import secrets

# MongoDB Connection

db_user = secrets.get('DATABASE_USER', 'root')
db_pass = secrets.get('DATABASE_PASSWORD', 'pass')

cluster = MongoClient(f'mongodb+srv://{db_user}:{db_pass}@robonatty-cluster.cykzb.mongodb.net/Store?retryWrites=true&w=majority')
db = cluster["Store"]
category_collection = db["Category"]
product_collection = db["Product"]

# Product Related
def index(request):
    return render(request, "index.html", {"name": "Alexa"})

# displays all product categories
def products(request):
    if request.method == "GET":
        controller = productsController()
        if controller == False:
            return render(request, "error_routes/error.html", {"message": "Unable to retrieve categories from our database." })

        return render(request, "product_routes/categories.html", {"data" : controller})

# displays all products in a specific category
def category(request, category):
    if request.method == "GET":
        controller = categoryController(category)
        if controller == False:
            return render(request, "error_routes/error.html", {"message": "Unable to retrieve products from our database." })
        return render(request, "product_routes/categories.html", {"data" : controller})

# displays a single product
def product(request, category, id):
    if request.method == "GET":
        singleProduct = product_collection.find_one({"_id": id})
        return render(request, "product_routes/product.html", {"data" : singleProduct})



# CONTROLLERS

def productsController():
    categoriesDict = {}
    try:
        categories = category_collection.find({})
        i = 0
        for category in categories:
            categoriesDict[i] = category
            i += 1
    except:
        return False
    return categoriesDict
    
    
def categoryController(category):
    productsDict = {}
    try:
        products = product_collection.find({"category" : category})
        i = 0
        for product in products:
            productsDict[i] = product
            i += 1
    
    except:
        return False
    return productsDict

def singleProductController(id):
    pass

        
