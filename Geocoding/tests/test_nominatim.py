import requests

from utils.api import NominatimApi

"""Прямое и обратное кодирование"""
class TestNominatim():

    def test_create_new_place(self):

        print("Метод POST")
        #  result_post: Response = Google_maps_api.create_new_place()  устаревшая конструкция
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Checking.check_status_code(result_post, 200) #  проверка статус0кода в тесте
        print(result_post.status_code)