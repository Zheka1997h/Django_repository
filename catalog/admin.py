from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Настройка админки для категорий"""
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Настройка админки для продуктов"""
    list_display = ('id', 'name', 'price', 'category')
    list_display_links = ('id', 'name')
    list_filter = ('category',)
    search_fields = ('name', 'description')