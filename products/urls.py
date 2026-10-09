from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.product_form, name='product_add'),
    path('products/<int:pk>/edit/', views.product_form, name='product_edit'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'), 
]