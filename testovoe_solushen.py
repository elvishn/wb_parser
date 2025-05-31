import requests


def extract_and_save_data(data):
    products = data.get("data", {}).get("products", [])
    for product in products:
        name = product.get("name", "No name")
        price = int(product.get("priceU", 0) / 100)
        product_info = {
            "Name": name,
            "Price": price,
        }
        return product_info
    return None  # Если товаров нет


def get_wb_product(article):
    base_url = "https://card.wb.ru/cards/detail?&dest=-1257786&nm={}".format(article)


    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Referer": "https://www.wildberries.ru/"
    }

    try:
        response = requests.get(base_url, headers=headers, timeout=10)
        if response.status_code == 200:
            card_data = response.json()
            content = extract_and_save_data(card_data)
            url = f"https://www.wildberries.ru/catalog/{article}/detail.aspx"
            return content
        else:
            print(f"Ошибка HTTP: {response.status_code}")
            return {"content": None, "url": None}

    except Exception as e:
        print(f"Ошибка соединения: {e}")
        return {"content": None, "url": None}


# Пример вызова
result = get_wb_product(228058513)
print(result)