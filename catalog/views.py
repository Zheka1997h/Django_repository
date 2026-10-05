from django.shortcuts import render


def home(request):
    """Контроллер главной страницы."""
    return render(request, 'catalog/home.html')


def contacts(request):
    """Контроллер страницы контактов с обработкой формы."""
    success = False

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Выводим данные в консоль
        print("\n" + "=" * 60)
        print("📨 ПОЛУЧЕНА ФОРМА ОБРАТНОЙ СВЯЗИ")
        print("-" * 60)
        print(f"  Имя: {name}")
        print(f"  Email: {email}")
        print(f"  Сообщение: {message}")
        print("=" * 60 + "\n")

        success = True

    return render(request, 'catalog/contacts.html', {'success': success})
