from django.urls import path
from . import views

urlpatterns = [
    # home
    path('', views.index, name='index'),

    # products
    path('categories/', views.categories),
    path('categories/<str:category>/', views.products),
    path('categories/<str:category>/<str:id>', views.singleProduct)
    
]