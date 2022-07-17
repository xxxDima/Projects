import json


text = [{'brand': 'ИЖ', 'model': 'Планета', 'age': 1979, 'params': '2 такта 345 см³', 'type_moto': 'классик', 'usd': 100, 'mileage': 3000, 'link': 'https://moto.av.by/bike/izh/planeta/22849888'}, {'brand': 'Hors', 'model': 'Alpha', 'age': 2015, 'params': '4 такта 110 см³', 'type_moto': 'минибайк', 'usd': 100, 'mileage': 10000, 'link': 'https://moto.av.by/bike/hors/alpha/100897351'}, {'brand': 'ИЖ', 'model': 'Планета', 'age': 2000, 'params': '2 такта 350 см³', 'type_moto': 'классик', 'usd': 100, 'mileage': 10000, 'link': 'https://moto.av.by/bike/izh/planeta/100972221'}, {'brand': 'Минск', 'model': 'ММВЗ', 'age': 2000, 'params': '2 такта 125 см³', 'type_moto': 'классик', 'usd': 100, 'mileage': 15000, 'link': 'https://moto.av.by/bike/minsk/mmvz/101009146'}, {'brand': 'Минск', 'model': 'C', 'age': 1992, 'params': '2 такта 120 см³', 'type_moto': 'спорт', 'usd': 100, 'mileage': 16000, 'link': 'https://moto.av.by/bike/minsk/c/101010037'}, {'brand': 'ИЖ', 'model': 'Планета', 'age': 2000, 'params': '2 такта 350 см³', 'type_moto': 'классик', 'usd': 100, 'mileage': 10000, 'link': 'https://moto.av.by/bike/izh/planeta/100972221'}, {'brand': 'Pannonia', 'model': 'T', 'age': 1975, 'params': '2 такта 250 см³', 'type_moto': 'классик', 'usd': 100, 'mileage': 30000, 'link': 'https://moto.av.by/bike/pannonia/t/100860292'}, {'brand': 'ИЖ', 'model': 'Планета', 'age': 2000, 'params': '2 такта 350 см³', 'type_moto': 'классик', 'usd': 100, 'mileage': 10000, 'link': 'https://moto.av.by/bike/izh/planeta/100972221'}, {'brand': 'ИЖ', 'model': 'Юпитер', 'age': 1984, 'params': '2 такта 350 см³', 'type_moto': 'классик', 'usd': 100, 'mileage': 11111, 'link': 'https://moto.av.by/bike/izh/yupiter/101071195'}, {'brand': 'BMW', 'model': 'K', 'age': 1994, 'params': '4 такта 1100 см³', 'type_moto': 'туризм', 'usd': 100, 'mileage': 100000, 'link': 'https://moto.av.by/bike/bmw/k/101092575'}, {'brand': 'Днепр', 'model': 'МТ-10-36', 'age': 1984, 'params': '4 такта 650 см³', 'type_moto': 'кастом', 'usd': 100, 'mileage': 300, 'link': 'https://moto.av.by/bike/dnepr/mt-10-36/101251754'}, {'brand': 'Минск', 'model': 'C', 'age': 1996, 'params': '2 такта 125 см³', 'type_moto': 'классик', 'usd': 100, 'mileage': 70000, 'link': 'https://moto.av.by/bike/minsk/c/101314846'}, {'brand': 'Pannonia', 'model': 'T', 'age': 1975, 'params': '2 такта 250 см³', 'type_moto': 'классик', 'usd': 100, 'mileage': 30000, 'link': 'https://moto.av.by/bike/pannonia/t/100860292'}, {'brand': 'ИЖ', 'model': 'Планета', 'age': 2000, 'params': '2 такта 350 см³', 'type_moto': 'классик', 'usd': 100, 'mileage': 10000, 'link': 'https://moto.av.by/bike/izh/planeta/100972221'}, {'brand': 'ИЖ', 'model': 'Юпитер', 'age': 1984, 'params': '2 такта 350 см³', 'type_moto': 'классик', 'usd': 100, 'mileage': 11111, 'link': 'https://moto.av.by/bike/izh/yupiter/101071195'}, {'brand': 'BMW', 'model': 'K', 'age': 1994, 'params': '4 такта 1100 см³', 'type_moto': 'туризм', 'usd': 100, 'mileage': 100000, 'link': 'https://moto.av.by/bike/bmw/k/101092575'}, {'brand': 'Днепр', 'model': 'МТ-10-36', 'age': 1984, 'params': '4 такта 650 см³', 'type_moto': 'кастом', 'usd': 100, 'mileage': 300, 'link': 'https://moto.av.by/bike/dnepr/mt-10-36/101251754'}, {'brand': 'Минск', 'model': 'C', 'age': 1996, 'params': '2 такта 125 см³', 'type_moto': 'классик', 'usd': 100, 'mileage': 70000, 'link': 'https://moto.av.by/bike/minsk/c/101314846'}]

a = json.dumps(text)
print(a)
print(type(a))















