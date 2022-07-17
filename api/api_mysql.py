from api_config import *


def ages_moto(age):
    command = f'select * from moto where age = "{age}";'
    return command


def price_moto(usd):
    command = f'select * from moto where usd = "{usd}";'
    return command


def connect(commands):
    try:
        # подкллючаемся к БД
        connection = pymysql.connect(host=host,
                                     user=user,
                                     port=3306,
                                     password=password,
                                     database=database,
                                     charset=charset,
                                     cursorclass=cursorclass)
        print("connect... OK")

        try:
            with connection.cursor() as cursor:
                cursor.execute(commands)
                rows = cursor.fetchall()
                return rows

        finally:
            connection.close()
            print("connection close... OK")

    except Exception as ex:
        # Если ошибка в подключении, то выводим тип ошибки
        print("no connect...")
        print(ex)




# def ages_moto(age):
#     with connection.cursor() as cursor:
#         cursor.execute(f'select * from moto where age = "{age}";')
#         rows = cursor.fetchall()
#         return rows


# def ages_moto(age):
#     """функция возвращает список по заданному параметру года int"""
#     list_motos_age = []
#     for i in rows:
#         if age == i['age']:
#             list_motos_age.append(i)
#         else:
#             continue
#     return list_motos_age

#
# def price_moto(price):
#     list_moto_price = []
#     for i in rows:
#         if price == i['usd']:
#             list_moto_price.append(i)
#         else:
#             continue
#     return list_moto_price

