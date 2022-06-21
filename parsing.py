import requests
from bs4 import BeautifulSoup
from re import sub, split
from math import ceil


URL = "https://moto.av.by/filter?category_type=1&price_usd[max]=200&page=1&sort=4"
HOST = "https://moto.av.by"

def get_html(url, params=None):
    """
    принимает URL адрес и если статус ок, возвращает объект <class 'requests.models.Response'>
    """
    r = requests.get(url, params=params)
    if r.status_code == 200:
        return r
    else:
        print("что-то пошло не так :( ...")


def page(url):
    """
    возвращает найденое количество страниц int
    """
    html = get_html(url).text
    soup = BeautifulSoup(html, 'html.parser')
    # находим запись 'На странице 25 объявлений из 3 884' на странице и делаем срез для получения количества объявлений
    count = soup.find('div', class_='paging__text').get_text().split(' ')
    num = (int(sub(' ', '', count[5]))) / 25  # по шаблону убираем лишние символы
    return ceil(num)


def one_list_moto(url, params=None):
    """
    возвращает результат поиска одной страницы
    (марку, модель, год выпуска, характеристики, тип, цену в USD, пробег, ссылку)
    """
    if params is None:
        params = {'page': 1}
    else:
        params = {'page': params}
        moto_list = []
        html = get_html(url, params=params)  # <class 'requests.models.Response'>
        soup = BeautifulSoup(html.text, 'html.parser')
        elements = soup.findAll('div', class_='listing-item')
        for element in elements:
            moto = {}
            brand = element.find('span', class_='link-text').get_text()
            # print({'111': brand})
            moto['brand'] = str(split(r' +', brand)[0])
            moto['model'] = str(split(r' +', brand)[1])
            params = str(element.find('div', class_='listing-item__params').get_text())
            # print({'params': params})

            age = split(r'\xa0', params)
            moto['age'] = int(age[0])

            param = (' '.join(split(r' +', (sub('\u2009', '', sub('\xa0', ' ', sub(f'{age[0]}\xa0г.', '', params)))))[0:4])).replace(',', '', -1)
            moto['params'] = str(param)

            type_moto = ((split(r' +', params))[2]).replace(',', '', -1)
            moto['type_moto'] = str(type_moto)

            price_usd = str(element.find('div', class_='listing-item__priceusd').get_text())
            moto['usd'] = int(sub('\xa0\$', '', (sub('≈\xa0', '', price_usd))))

            mileage = sub(r'\xa0км', '', (sub(r'\u2009', '', ((split(r' ', params))[3]))))
            moto['mileage'] = int(mileage)

            link = element.find('a', class_='listing-item__link').get('href')
            moto['link'] = str(HOST+link)

            # price_byn = element.find('div', class_='listing-item__price').get_text()
            # moto.append({'byn': int(sub(r'\xa0р.', '', (sub(r'\u2009', ' ', price_byn))))})
            moto_list.append(moto)

        return moto_list


def parser(url):
    """
    возвращает список всех найденых мотоциклов (марку, характеристики, цену в USD, цену в BYN)
    """
    all_moto_list = []
    paiges = page(url)
    for paige in range(1, paiges + 1):
        print(f'выполняется процесс парсинга страницы {paige} из {paiges}')
        all_moto_list.extend(one_list_moto(url, paige))
    return all_moto_list



