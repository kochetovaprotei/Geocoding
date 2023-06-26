import requests

from utils.api import NominatimApi
import pytest

"""Прямое и обратное кодирование"""


class TestNominatim():

    @pytest.mark.parametrize('name, expected_latitude, expected_longitude', [()])
    def test_create_new_place(name, expected_latitude, expected_longitude):

        print("Метод Get сравнение координат из ответа ")
        #  result_post: Response = Google_maps_api.create_new_place()  устаревшая конструкция
        result_search_by_name = NominatimApi.search_by_name()
        check_coordinates = result_search_by_name.json()
        check_info_lat = check_coordinates.get('lat')  # сохраняем значение ключа ширины
        check_info_lon = check_coordinates.get('lon')  # сохраняем значение ключа долготы

        print(check_info_lat)
        print(check_info_lon)

        assert
