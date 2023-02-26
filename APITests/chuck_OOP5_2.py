import requests

class TestNewJoke:
    '''Создание новой шутки'''
    def __init__(self):
        pass

    def create_new_random_joke(self):
        '''Создание случаайной шутки'''
        url = 'https://api.chucknorris.io/jokes/random'
        print(url)
        result = requests.get(url)  # отправляем запрос апи
        print('Status code: ' + str(result.status_code))  # запрашиваем статус код из ответа
        assert 200 == result.status_code  # сравнимваем значение с выводимыми

        result.encoding = 'utf-8'  # чтобы формат ответа приводился к единому
        print('Response: ' + result.text)  # текст тела ответа
        check = result.json()  # ответ из запроса в виде json
        check_info = check.get('categories')  # сохраняем значение ключа categories
        print(check_info)
        assert check_info == []   # проверяем значение ключа categories
        print('Right category')

        check_info_value = check.get('value')  # сохраняем значение ключа value
        print(check_info_value)
        name = 'Chuck'
        if name in check_info_value:
            print('Chuck is here')  # проверяем значение ключа value - это наличие шутки
        else:
            print("Chuck isn't here!")


random_joke = TestNewJoke()
random_joke.create_new_random_joke()


