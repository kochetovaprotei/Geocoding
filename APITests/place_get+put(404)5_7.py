import requests


class TestNewLocation:
    """Работа с новой локацией"""

    def test_create_new_location(self):
        """Создание новой локации"""

        base_url = 'https://rahulshettyacademy.com'  # базовая url
        key = '?key=qaclick123'  # параметр для всех запросов
        post_resource = '/maps/api/place/add/json'  # ресурс пост

        #
        # """ПРоверка существования новой локации"""
        # place_id ='5555'
        # get_resource = '/maps/api/place/get/json'
        # get_url = base_url + get_resource + key + '&place_id=' + place_id
        # print(get_url)
        # result_get = requests.get(get_url)
        # print(result_get.text)
        #
        # print('Status-code: ' + str(result_get.status_code))
        # assert 404 == result_get.status_code
        # print("Status get is wrong! Location doesn't exist!")

        """Изменение новой локации"""
        put_resource = '/maps/api/place/update/json'
        put_url = base_url + put_resource + key
        print(put_url)
        json_for_update_new_location = {
            "place_id": '5555',
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = requests.put(put_url, json=json_for_update_new_location)
        print(result_put.text)

        print('Status-code: ' + str(result_put.status_code))
        assert 404 == result_put.status_code
        print("Status get is wrong! Location doesn't exist!")

        check_put = result_put.json()
        check_put_info = check_put.get('msg')
        print(check_put_info)
        print('Message from response: ' + check_put_info)
        assert check_put_info == 'Address successfully updated'
        print('Message is right')


new_place = TestNewLocation()
new_place.test_create_new_location()


