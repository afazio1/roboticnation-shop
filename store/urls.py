from django.urls import path
from . import views

urlpatterns = [
    # home
    path('', views.index, name='index'),
    path('cart/', views.cart),
    # products
    path('categories/', views.products),
    path('categories/<str:category>/', views.category),
    path('categories/<str:category>/<str:id>', views.product)
    
]