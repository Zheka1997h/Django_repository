from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Contact
from .forms import ProductForm  # ← понадобится для доп. задания
from django.core.paginator import Paginator  # ← для пагинации


def home_page(request):
    """Главная страница - вывод всех продуктов с пагинацией"""
    products_list = Product.objects.all()  # ← Лаконичный запрос по ТЗ

    # Пагинация (доп. задание)
    paginator = Paginator(products_list, 6)  # по 6 товаров на странице
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'catalog/home.html', {'products': products})


def product_detail(request, pk):
    """Страница с подробной информацией о товаре"""
    product = get_object_or_404(Product, pk=pk)  # ← Извлекаем через ORM
    return render(request, 'catalog/product_detail.html', {'product': product})


def contacts_page(request):
    """Страница контактов"""
    contacts = Contact.objects.all()
    return render(request, 'catalog/contacts.html', {'contacts': contacts})


def add_product(request):
    """Добавление нового товара (доп. задание)"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:home')
    else:
        form = ProductForm()
    return render(request, 'catalog/add_product.html', {'form': form})