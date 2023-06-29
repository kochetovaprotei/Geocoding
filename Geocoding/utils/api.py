# import requests
import json
# from utils.http_methods import HttpMethods
#
# """Методы для прямого и обратного геокодирования"""
#
# base_url = 'https://nominatim.openstreetmap.org/'
# format_json = '&format=jsonv2'
#
#
class NominatimApi():
#
#     """Метод для прямого кодирования"""
#     @staticmethod
#     def search_by_name():

    @staticmethod
    def search_by_name():
        with open('/home/kochetova/PycharmProjects/pythonProject1/Geocoding/utils/data_for_searching_by_name.json', 'r',
                  encoding='utf-8') as f:
            temp_data = json.load(f)
            data = []
            for i in temp_data:
                data.append(temp_data[i])
            # print(data)
        return data


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
    #


