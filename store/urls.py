from django.urls import path
from . import views

urlpatterns = [
    # home
    path('', views.index, name='index'),

    # products
    path('products/', views.products),
    path('products/<str:category>/', views.category),
    path('products/<str:category>/<str:id>', views.product)
    
]