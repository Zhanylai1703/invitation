import requests
from bs4 import BeautifulSoup

# URL страницы
url = "https://eventsletter.ru/wedding/rose"

# Заголовки, имитирующие запрос от браузера
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# Получаем содержимое страницы с поддельными заголовками
response = requests.get(url, headers=headers)

# Проверка успешности запроса
if response.status_code == 200:
    # Парсинг HTML-кода страницы
    soup = BeautifulSoup(response.text, 'html.parser')

    # Сохранение HTML-кода в файл
    with open("templates/page_source.html", "w", encoding="utf-8") as file:
        file.write(soup.prettify())

    print("HTML-код успешно сохранен в файл page_source.html")
else:
    print(f"Не удалось получить страницу, код ошибки: {response.status_code}")
