import requests


class FindLocation:
    """Найти локацию"""


    def search_location_by_name(self):
        """Поиск локации по названию"""

        base_url = 'https://nominatim.openstreetmap.org/'
        get_resource = 'search.php?'
        query = 'q=иорданский+пруд'
        format_json = '&format=jsonv2'
        get_url = base_url + get_resource + query + format_json
        print(get_url)
        result = requests.get(get_url)  # отправляем запрос апи
        print('Status code: ' + str(result.status_code))  # запрашиваем статус код из ответа
        assert 200 == result.status_code  # сравнимваем значение с выводимыми
        print('We found your address!')
        result.encoding = 'utf-8'  # чтобы формат ответа приводился к единому
        print('Response: ' + result.text)  # текст тела ответа

        check = result.json()  # ответ из запроса в виде json
        check_info_responce = check[0]

        check_info_lat = check_info_responce.get('lat')  # сохраняем значение ключа ширины
        check_info_lon = check_info_responce.get('lon')  # сохраняем значение ключа долготы

        print(check_info_lat)
        print(check_info_lon)

        assert check_info_lat == '59.99357575'  # проверяем значение ключа ширины
        print('Right latitude!')
        assert check_info_lon == '30.3362719762346'  # проверяем значение ключа долготы
        print('Right longitude!')

    def search_location_by_coordinates(self):
        """Поиск локации по координатам"""

        base_url = 'https://nominatim.openstreetmap.org/'
        get_resource = 'reverse?'
        lat_value = '59.99357575'
        lon_value = '30.3362719762346'
        format_json = 'format=jsonv2&'
        get_url = base_url + get_resource + format_json + 'lat=' + lat_value + '&lon=' + lon_value
        print(get_url)
        result = requests.get(get_url)  # отправляем запрос апи
        print('Status code: ' + str(result.status_code))  # запрашиваем статус код из ответа
        assert 200 == result.status_code  # сравнимваем значение с выводимыми
        print('We found your address!')
        result.encoding = 'utf-8'  # чтобы формат ответа приводился к единому
        print('Response: ' + result.text)  # текст тела ответа

        check = result.json()  # ответ из запроса в виде json
        check_info_address = check.get('display_name')  # сохраняем значение ключа адреса

        print('Address is: ' + check_info_address)
        assert check_info_address == 'аллея Кайгородова, Лесной, округ Светлановское, Санкт-Петербург, Северо-Западный федеральный округ, 194153, Россия'
        print('Right address!')


find_location = FindLocation()
find_location.search_location_by_name()
find_location.search_location_by_coordinates()
