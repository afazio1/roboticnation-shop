from django.urls import path
from . import views

urlpatterns = [
    # home
    path('', views.index, name='index'),

    # products
<<<<<<< HEAD
    path('categories/', views.categories),
    path('categories/<str:category>/', views.products),
    path('categories/<str:category>/<str:id>', views.singleProduct)
=======
    path('categories/', views.products),
    path('categories/<str:category>/', views.category),
    path('categories/<str:category>/<str:id>', views.product)
>>>>>>> 9ac041b28d3d6cde1433ee5560bcfa73b176e347
    
]