## 3. Файл `server.py`
"""
WebShop — простое веб-приложение на стандартной библиотеке Python.
Обработчик HTTP-запросов без использования фреймворков.

Маршруты:
  GET  /           -> главная страница (Категория с товарами)
  GET  /contacts/  -> страница контактов
  POST /contacts/  -> обработка формы обратной связи
"""

import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs


# ─────────────────────────────────────────────────────────────
# Настройка путей
# ─────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")


def read_template(filename: str) -> str:
    """
    Читает HTML-шаблон из файла с помощью контекстного менеджера.

    Args:
        filename: имя файла шаблона (например, 'contacts.html')

    Returns:
        Содержимое файла в виде строки (UTF-8)

    Raises:
        FileNotFoundError: если файл не найден
    """
    filepath = os.path.join(TEMPLATES_DIR, filename)
    # Отладка: выводим путь
    print(f"\n[DEBUG] Ищем файл: {filepath}")
    print(f"[DEBUG] TEMPLATES_DIR: {TEMPLATES_DIR}")
    print(f"[DEBUG] Файл существует: {os.path.isfile(filepath)}")
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


# ─────────────────────────────────────────────────────────────
# Обработчик HTTP-запросов
# ────────────────────────────────────────────────────────────
class WebShopHandler(BaseHTTPRequestHandler):
    """HTTP-обработчик для приложения WebShop."""

    # Карта маршрутов: путь -> имя шаблона
    ROUTES = {
        "/": "home.html",
        "/home/": "home.html",
        "/contacts/": "contacts.html",
        "/contacts": "contacts.html",
    }

    # ─────────────────────────────────────────────────────────
    # GET-запросы
    # ─────────────────────────────────────────────────────────
    def do_GET(self):
        """
        Обрабатывает GET-запросы.
        Возвращает HTML-страницу с заголовком Content-Type: text/html.
        """
        try:
            template_name = self.ROUTES.get(self.path)
            print(f"[DEBUG] Найден шаблон: {template_name}")

            if template_name is None:
                # Маршрут не найден — отдаём 404
                print(f"[DEBUG] Маршрут не найден, отдаём 404")
                self._send_error_page(404, "404.html")
                return

            # Чтение файла через контекстный менеджер
            html_content = read_template(template_name)

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html_content.encode("utf-8"))

        except FileNotFoundError:
            self._send_error_page(404, "404.html")
        except Exception as e:
            print(f"[ERROR] Ошибка при обработке GET: {e}")
            self._send_error_page(500, "500.html")

    # ─────────────────────────────────────────────────────────
    # POST-запросы (дополнительное задание)
    # ─────────────────────────────────────────────────────────
    def do_POST(self):
        """
        Обрабатывает POST-запросы.
        Принимает данные формы и выводит их в консоль.
        """
        try:
            # Читаем тело запроса
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")

            # Парсим данные формы (application/x-www-form-urlencoded)
            parsed_data = parse_qs(body)

            # Выводим данные в консоль
            print("\n" + "=" * 60)
            print(" ПОЛУЧЕН POST-ЗАПРОС")
            print(f"📍 Путь: {self.path}")
            print("-" * 60)
            print("📝 Данные от пользователя:")
            for key, values in parsed_data.items():
                print(f"   • {key}: {values[0]}")
            print("=" * 60 + "\n")

            # Отправляем ответ пользователю
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()

            response = self._build_success_page(parsed_data)
            self.wfile.write(response.encode("utf-8"))

        except Exception as e:
            print(f"[ERROR] Ошибка при обработке POST: {e}")
            self._send_error_page(500, "500.html")

    # ─────────────────────────────────────────────────────────
    # Вспомогательные методы
    # ─────────────────────────────────────────────────────────
    def _send_error_page(self, status_code: int, template_name: str):
        """Отправляет страницу ошибки с указанным статус-кодом."""
        try:
            html_content = read_template(template_name)
            self.send_response(status_code)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html_content.encode("utf-8"))
        except Exception:
            self.send_response(status_code)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(f"Error {status_code}".encode("utf-8"))

    def _build_success_page(self, data: dict) -> str:
        """Формирует HTML-страницу успешной отправки формы."""
        name = data.get("name", ["Гость"])[0]
        return f"""
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <title>WebShop — Сообщение отправлено</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body class="bg-light">
            <div class="container mt-5">
                <div class="card shadow">
                    <div class="card-body text-center py-5">
                        <h1 class="text-success mb-4">✅ Спасибо, {name}!</h1>
                        <p class="lead">Ваше сообщение успешно отправлено. Мы свяжемся с вами в ближайшее время.</p>
                        <a href="/contacts/" class="btn btn-primary mt-3">← Вернуться к контактам</a>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """

    def log_message(self, format, *args):
        """Переопределяем логирование для удобства."""
        print(f"[{self.log_date_time_string()}] {format % args}")


# ─────────────────────────────────────────────────────────────
# Запуск сервера
# ────────────────────────────────────────────────────────────
def run_server(host: str = "127.0.0.1", port: int = 8080):
    """Запускает HTTP-сервер."""
    server = HTTPServer((host, port), WebShopHandler)
    print("=" * 60)
    print("🚀 WebShop Server запущен!")
    print(f" Главная:    http://{host}:{port}/")
    print(f"📍 Контакты:   http://{host}:{port}/contacts/")
    print("⏹  Для остановки нажмите Ctrl+C")
    print("=" * 60)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n Сервер остановлен.")
        server.server_close()


if __name__ == "__main__":
    run_server()