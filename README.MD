# Django Shop - Учебный проект интернет-магазина

Учебный проект интернет-магазина на Django с подключением PostgreSQL, моделями продуктов и категорий, админ-панелью и кастомными командами управления.

## 🚀 Технологии

- **Python 3.10+**
- **Django 4.2.7**
- **PostgreSQL** - основная база данных
- **psycopg2-binary** - драйвер для PostgreSQL
- **Pillow** - работа с изображениями
- **ipython** - улучшенная интерактивная оболочка
- **python-dotenv** - управление переменными окружения

## 📁 Структура проекта


Django_Project/
├── manage.py # Утилита командной строки Django
├── requirements.txt # Зависимости проекта
├── .env # Переменные окружения (не коммитится)
├── .env.example # Шаблон переменных окружения
├── .gitignore # Игнорируемые файлы
├── README.md # Документация проекта
│
├── config/ # Настройки проекта
│ ├── settings.py # Основные настройки
│ ├── urls.py # Корневые URL-маршруты
│ ├── wsgi.py # WSGI конфигурация
│ └── asgi.py # ASGI конфигурация
│
├── catalog/ # Приложение каталога
│ ├── models.py # Модели Category, Product, Contact
│ ├── admin.py # Настройки админ-панели
│ ├── views.py # Контроллеры (представления)
│ ├── urls.py # Маршруты приложения
│ ├── migrations/ # Миграции базы данных
│ ├── fixtures/ # Фикстуры для тестовых данных
│ │ ├── categories.json
│ │ └── products.json
│ └── management/ # Кастомные команды
│ └── commands/
│ └── populate_db.py
│
├── templates/ # HTML шаблоны
│ └── catalog/
│ ├── base.html # Базовый шаблон
│ ├── home.html # Главная страница
│ └── contacts.html # Страница контактов
│
├── static/ # Статические файлы
│ └── css/
│ └── style.css # Стили
│
├── media/ # Загруженные пользователями файлы
│ └── products/ # Изображения продуктов
│
└── screenshots/ # Скриншоты для домашки


## 🛠️ Установка и запуск

### 1. Клонирование репозитория

```bash
git clone <url-репозитория>
cd Django_Project


Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```





