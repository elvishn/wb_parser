import requests


def extract_and_save_data(data):
    products = data.get("data", {}).get("products", [])  # Достаем список товаров
    for product in products:
        name = product.get("name", "No name")  # Название товара (или "No name" если нет)
        price = int(product.get("priceU", 0) / 100)  # Цена (делим на 100 для руб.)
        return {  # Возвращаем словарь с данными
            "Name": name,
            "Price": price,
        }
    return None  # Если товаров нет в ответе


def get_wb_product(article):
    # Формируем URL запроса с артикулом товара
    base_url = "https://card.wb.ru/cards/detail?&dest=-1257786&nm={}".format(article)

    # Заголовки для имитации браузера
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        # Имитация Chrome
        "Accept": "application/json", # Запрос данных в JSON
        "Referer": "https://www.wildberries.ru/" # Откуда пришли
    }

    try:
        # Отправляем GET-запрос к API Wildberries
        response = requests.get(base_url, headers=headers, timeout=10)
        if response.status_code == 200: # Если успешный ответ
            card_data = response.json() # Парсим JSON
            content = extract_and_save_data(card_data) # Извлекаем данные
            return content # Возвращаем информацию о товаре
        else: # Если ошибка HTTP
            print(f"Ошибка HTTP: {response.status_code}")
            return {"content": None, "url": None}

    except Exception as e: # Если проблемы с соединением
        print(f"Ошибка соединения: {e}")
        return {"content": None, "url": None}


# Пример вызова
result = get_wb_product(228058513)
print(result)