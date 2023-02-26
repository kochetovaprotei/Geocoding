import requests


class TestNewLocation:
    """Работа с новой локацией"""

    def test_create_new_location(self):
        """Создание новой локации"""

        base_url = 'https://rahulshettyacademy.com'  # базовая url
        key = '?key=qaclick123'  # параметр для всех запросов
        post_resource = '/maps/api/place/add/json'  # ресурс пост

        """Создание новой локации post"""
        post_url = base_url + post_resource + key
        print(post_url)

        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        result_post = requests.post(post_url, json=json_for_create_new_location)  # сохраняем запрос с
        # данными url и body
        print(result_post.text)
        print('Status code: ' + str(result_post.status_code))  #
        assert 200 == result_post.status_code
        print('Status post is successfull!')

        check_post = result_post.json()
        check_info_post = check_post.get('status')  # получаем статус-код из тела запроса (в каком-то поле, значении)
        print('Status-code: ' + check_info_post)
        assert check_info_post == 'OK'
        print('Status is right!')

        place_id = check_post.get('place_id')
        print('Place_id: ' + place_id)

        """ПРоверка создания новой локации"""
        get_resource = '/maps/api/place/get/json'
        get_url = base_url + get_resource + key + '&place_id=' + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)

        print('Status-code: ' + str(result_get.status_code))
        assert 200 == result_get.status_code
        print('Status get is right!')

        """Изменение новой локации"""
        put_resource = '/maps/api/place/update/json'
        put_url = base_url + put_resource + key
        print(put_url)
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = requests.put(put_url, json=json_for_update_new_location)
        print(result_put.text)

        print('Status-code: ' + str(result_put.status_code))
        assert 200 == result_put.status_code
        print('Status code put is right!')

        check_put = result_put.json()
        check_put_info = check_put.get('msg')
        print(check_put_info)
        print('Message from response: ' + check_put_info)
        assert check_put_info == 'Address successfully updated'
        print('Message is right')

        """Проверка обновления новой локации"""
        result_get = requests.get(get_url)
        print(result_get.text)

        print('Status-code: ' + str(result_get.status_code))
        assert 200 == result_get.status_code
        print('Status updated location is right!')
        """Проверка адреса"""
        check_address = result_get.json()
        check_address_info = check_address.get('address')
        print('Message from response: ' + check_address_info)
        assert check_address_info == '100 Lenina street, RU'
        print('Address is matched')

new_place = TestNewLocation()
new_place.test_create_new_location()
