import requests
from utils.http_methods import HttpMethods

"""Методы для прямого и обратного геокодирования"""

base_url = 'https://nominatim.openstreetmap.org/'
format_json = '&format=jsonv2'


class NominatimApi():

    """Метод для прямого кодирования"""
    @staticmethod
    def search_by_name():

        filename = 'search.php?'
        search_url = base_url + filename + query + format_json
        print(search_url)
        result_search_by_name = HttpMethods.search_and_reverse(search_url)

        print(result_search_by_name.text)
        return result_search_by_name

    """Метод для обратного кодирования"""
    @staticmethod
    def reverse_by_coordinate(place_id):

        filename = 'reverse.php?'
        reverse_url = base_url + filename + query + format_json
        print(reverse_url)
        result_reverse_by_coordinate = HttpMethods.search_and_reverse(reverse_url)
        print(result_reverse_by_coordinate.text)
        return result_reverse_by_coordinate



