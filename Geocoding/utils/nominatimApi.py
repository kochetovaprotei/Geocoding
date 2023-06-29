import requests
from utils.utils_for_file import GetDataFromFile

"""Методы для прямого и обратного геокодирования"""

base_url = 'https://nominatim.openstreetmap.org/'
format_json = '&format=jsonv2'


class NominatimApi:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod  # чтобы не привязываться к конкретному классу
    def search():
        abv = GetDataFromFile.data_from_first_file()
        print(abv['input_data'])
        filename = 'search.php?'
        query = GetDataFromFile.data_from_first_file.test_data['input_data']
        search_url = base_url + filename + query + format_json
        print(search_url)
        result = requests.get(search_url, headers=NominatimApi.headers, cookies=NominatimApi.cookie)
        return result

new = NominatimApi
new.search()

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
