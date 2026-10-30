from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('contacts/', views.contacts_page, name='contacts'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('add-product/', views.add_product, name='add_product'),  # ← НОВОЕ
]