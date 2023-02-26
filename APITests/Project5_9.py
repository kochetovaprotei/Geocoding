import requests


class NewLocation:
    """Работа с новой локацией"""

    def test_post_new_location(self):
        """Создание новой локации"""

        base_url = 'https://rahulshettyacademy.com'  # базовая url
        key = '?key=qaclick123'  # параметр для всех запросов
        post_resource = '/maps/api/place/add/json'  # ресурс пост

        """Создание новой локации post"""
        post_url = base_url + post_resource + key
        print(post_url)

        json_for_post_new_location = {
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

        for i in range(5):
            result_post = requests.post(post_url, json=json_for_post_new_location)  # сохраняем запрос с
            # данными url и body
            print(result_post.text)

            check_post = result_post.json()
            place_id = check_post.get('place_id')

            fw = open('file_place_id.txt', 'a')  # создать файл и выполняет действие a, права на запись
            fw.write(place_id + '\n')  # записать строку с переносом строки
            fw.close()

            print('Status code: ' + str(result_post.status_code))
            assert 200 == result_post.status_code
            print('New location is created!')

        """ПРоверка place_id локации из текстового файла"""
        fr = open('file_place_id.txt', 'r')
        place_id_from_txt = fr.readline(32)
        fr.close()

        get_resource = '/maps/api/place/get/json'
        get_url = base_url + get_resource + key + '&place_id=' + place_id_from_txt
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)

        print('Status-code: ' + str(result_get.status_code))
        assert 200 == result_get.status_code
        print('New location had got from txt!')


send_get_to_read_place_id = NewLocation()
send_get_to_read_place_id.test_post_new_location()
