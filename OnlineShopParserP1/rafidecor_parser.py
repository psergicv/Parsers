import requests
import json
from bs4 import BeautifulSoup

# 219, 32, 16
urls_dict = {
    'ro/pages/catalog/tapet/': 2,
    'ro/pages/catalog/covoare/': 2,
    'ro/pages/catalog/lepnina/': 2
}

url = 'https://rafidecor.md/'

lista_tapete, lista_covoare, lista_lepnina = [], [], []

for k, v in urls_dict.items():
    total_pages = v
    for page in range(1, total_pages + 1):
        full_url = url + k + str(page)
        response = requests.get(full_url)
        html_page = response.content
        soup = BeautifulSoup(html_page, 'lxml')

        all_divs = soup.find_all('div', class_='item__review')

        filename = k.split('/')[-2]

        for item in all_divs:
            product_name = item.find('a', class_='name').text.strip()
            in_stock = item.find('div', class_='item_status').text.strip()
            article_nr = item.find('div', class_='art').text.strip()
            product_price = item.find('div', class_='item_price').text.strip()

            if 'tapet' in k:
                lista_tapete.append([article_nr, product_name, product_price, in_stock])
            elif 'covoare' in k:
                lista_covoare.append([article_nr, product_name, product_price, in_stock])
            else:
                lista_lepnina.append([article_nr, product_name, product_price, in_stock])

    if 'tapet' in k:
        with open(f"json_folder/rafidec/{filename}_product_list.json", 'w', encoding='utf-8') as f:
            json.dump(lista_tapete, f, ensure_ascii=False, indent=4)
    elif 'covoare' in k:
        with open(f"json_folder/rafidec/{filename}_product_list.json", 'w', encoding='utf-8') as f:
            json.dump(lista_covoare, f, ensure_ascii=False, indent=4)
    else:
        with open(f"json_folder/rafidec/{filename}_product_list.json", 'w', encoding='utf-8') as f:
            json.dump(lista_lepnina, f, ensure_ascii=False, indent=4)
