import requests
from utils.utils_for_file import GetDataFromFile


"""Методы для прямого и обратного геокодирования"""

base_url = 'https://nominatim.openstreetmap.org/'
format_json = '&format=jsonv2'
date_request = GetDataFromFile.data_from_first_file()
print(date_request)


class NominatimApi:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod  # чтобы не привязываться к конкретному классу
    def search(query):
        filename = 'search.php?'
        # query_dict = date_request[0]
        # query = query_dict['input_data']
        # query = date_request[0]['input_data']
        print(query)
        search_url = base_url + filename + str(query) + format_json
        print(search_url)
        result = requests.get(search_url, headers=NominatimApi.headers, cookies=NominatimApi.cookie)
        result.encoding = 'utf-8'
        print(result.text)
        # добавить проверки на статус код
        check_info_responce = result.json()[0]  # ответ из запроса в виде json
        # убрать оставить только резалт, остальное вызывать в тесте
        check_info_lat = check_info_responce.get('lat')  # сохраняем значение ключа ширины
        check_info_lon = check_info_responce.get('lon')  # сохраняем значение ключа долготы

        check_info_lat_and_lon = [check_info_lat, check_info_lon]

        print(check_info_lat)
        print(check_info_lon)
        print(check_info_lat_and_lon)
        return check_info_lat_and_lon


# NominatimApi.search()

# find_location = NominatimApi
# find_location.search(test_data['input_data'])


# @staticmethod  # чтобы не привязываться к конкретному классу
# def reverse(url):
#     result = requests.get(url, headers=NominatimApi.headers, cookies=NominatimApi.cookie)
#     return result


#     filename = 'search.php?'
#     search_url = base_url + filename + query + format_json
#     print(search_url)
#     result_search_by_name = HttpMethods.search_and_reverse(search_url)
#
#     print(result_search_by_name.text)
#     return result_search_by_name
#
# """Метод для обратного кодирования"""
# @staticmethod
# def reverse_by_coordinate(place_id):
#
#     filename = 'reverse.php?'
#     reverse_url = base_url + filename + query + format_json
#     print(reverse_url)
#     result_reverse_by_coordinate = HttpMethods.search_and_reverse(reverse_url)
#     print(result_reverse_by_coordinate.text)
#     return result_reverse_by_coordinate
