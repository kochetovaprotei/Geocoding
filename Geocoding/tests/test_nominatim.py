import requests

from utils.api import NominatimApi
import pytest

"""Прямое и обратное кодирование"""


@pytest.mark.parametrize("test_data", NominatimApi.search_by_name())
def test_check_from_file(test_data):
    # NominatimApi.search_by_name()
    print(f"\nhttp - {test_data['input_data']}")
    print(f"\nresult - {test_data['result']}")
    pass

# class TestNominatim():
#
#     @pytest.mark.parametrize('query, expected_latitude, expected_longitude', [('q=иорданский+пруд', 59.99357575, 30.3362719762346),
#                                                                              ('q=артиллерийский+остров', 59.95330165, 30.314422577473174),
#                                                                              ('q=тортилин+пруд', 54.963702049999995, 20.489817549516772)])
#     def test_create_new_place(query, expected_latitude, expected_longitude):
#
#         print("Метод Get сравнение координат из ответа ")
#         #  result_post: Response = Google_maps_api.create_new_place()  устаревшая конструкция
#         result_search_by_name = NominatimApi.search_by_name()
#         check_coordinates = result_search_by_name.json()
#         check_info_lat = check_coordinates.get('lat')  # сохраняем значение ключа ширины
#         check_info_lon = check_coordinates.get('lon')  # сохраняем значение ключа долготы
#
#         print(check_info_lat)
#         print(check_info_lon)
#
#         assert
