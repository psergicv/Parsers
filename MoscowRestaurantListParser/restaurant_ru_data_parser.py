"""


"""
import requests
import json
from bs4 import BeautifulSoup

number_of_pages = 41
page_counter = 0
restaurant_dict = dict()

for page in range(1, number_of_pages+1):

    url = f'https://www.restoran.ru/msk/catalog/restaurants/all/?page={page}'

    response = requests.get(url)
    html_page = response.text

    soup = BeautifulSoup(html_page, 'lxml')

    all_restaurants = soup.find_all('div', class_='item')

    # restaurant_dict = dict()

    for rest in all_restaurants:
        try:
            restaurant_name = rest.find('a', class_='name').text
            restaurant_dict[restaurant_name] = dict()

            average_bill = rest.find('span', class_='average-bill').text
            restaurant_dict[restaurant_name]["Average bill"] = average_bill

            restaurant_type = rest.find('div', class_='prop').text
            restaurant_dict[restaurant_name]["Restaurant type"] = restaurant_type

            work_time = rest.find('div', class_='work-time').text.strip()
            restaurant_dict[restaurant_name]["Working hours"] = work_time

            phone = rest.find('a', class_='booking').text.strip()
            restaurant_dict[restaurant_name]["Phone number"] = phone

            address = rest.find('div', class_='value').text.strip()
            restaurant_dict[restaurant_name]["Address"] = address

            parking = rest.find('div', class_='parking').text.strip()
            restaurant_dict[restaurant_name]["Parking"] = parking
        except AttributeError:
            print('Error while parsing')

    with open('json_folder/moscow_restaurants.json', 'w', encoding='utf-8') as f:
        json.dump(restaurant_dict, f, ensure_ascii=False, indent=4)

    page_counter += 1
    print(f'Parsing progress {page_counter}/41')