 # 1. Отправить запрос Get который будет подставлять данные из текстового файла location_data.txt
 # 2. Убедиться, что запрос отправился корректно
 # 3. Сравнить данные из полученного ответа с данными из текстового файла expected_data.txt

import requests


class GetCoordinatesByName:
    """Получить координаты по имени"""


    def compare_coordinates_with_expected(self):
        """Сравнить координаты с ожидаемыми"""

        base_url = 'https://nominatim.openstreetmap.org/'
        get_resource = 'search.php?'

        fr = open('utils/data_for_searching_by_name.json', 'r')
        query = fr.read()  # читаем строчку из файла
        fr.close()

        format_json = '&format=jsonv2'

        get_url = base_url + get_resource + query + format_json
        print(get_url)
        result = requests.get(get_url)  # сохраняем тело ответа запроса get в переменную result

        print('Status code: ' + str(result.status_code))  # запрашиваем статус код из ответа
        assert 200 == result.status_code  # сравнимваем значение с выводимым статус кодом
        result.encoding = 'utf-8'  # чтобы формат ответа приводился к единому

        print('Response: ' + result.text)  # выводим текст тела ответа

        check = result.json()  # ответ из запроса в виде json
        check_info_responce = check[0]

        check_info_lat = check_info_responce.get('lat')  # сохраняем значение ключа ширины
        check_info_lon = check_info_responce.get('lon')  # сохраняем значение ключа долготы

        print(check_info_lat)
        print(check_info_lon)

        fr = open('utils/data_for_searching_by_coordinates.json', 'r')
        line_latitude = fr.readlines()  # читаем строчку из файла
        expected_latitude = line_latitude[0].rstrip()
        fr.close()

        assert check_info_lat == expected_latitude  # сравниваем значение ожидаемой ширины

        fr = open('utils/data_for_searching_by_coordinates.json', 'r')
        line_longitude = fr.readlines()  # читаем строчку из файла
        expected_longitude = line_longitude[1].rstrip()
        fr.close()

        assert check_info_lon == expected_longitude  # сравниваем значение ожидаемой долготы


find_location = GetCoordinatesByName()
find_location.compare_coordinates_with_expected()

