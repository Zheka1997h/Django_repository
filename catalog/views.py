from django.shortcuts import render
from .models import Product, Contact


def home_page(request):
    """Главная страница - вывод последних 5 продуктов"""
    # Получаем последние 5 продуктов
    latest_products = Product.objects.order_by('-created_at')[:5]

    # Выводим в консоль (терминал, где запущен runserver)
    print("\n=== Последние 5 продуктов ===")
    for product in latest_products:
        print(f"Продукт: {product.name} | Цена: {product.price} | Категория: {product.category.name}")
    print("=============================\n")

    return render(request, 'catalog/home.html', {'products': latest_products})


def contacts_page(request):
    """Страница контактов"""
    contacts = Contact.objects.all()
    return render(request, 'catalog/contacts.html', {'contacts': contacts})
