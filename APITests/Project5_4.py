import requests


class JokeFromCategory:
    """Создание шутки из категории"""
    def __init__(self):
        pass

    def get_categories(self):
        """Получение всех категорий"""
        url = 'https://api.chucknorris.io/jokes/categories'
        print(url)
        result = requests.get(url)  # сохраняем запрос апи
        print('Status code: ' + str(result.status_code))  # запрашиваем статус код из ответа
        assert 200 == result.status_code  # сравнимваем значение с выводимыми
        print('Status code is successfull!')
        result.encoding = 'utf-8'  # чтобы формат ответа приводился к единому
        print('All categories: ' + result.text)  # текст тела ответа

    def get_joke_from_category(self):
        """Создание шутки из категории"""
        url = 'https://api.chucknorris.io/jokes/categories'
        result = requests.get(url)
        category = result.json()

        for i in category:  # вместо счетчика i подставляем элементы списка category для вывода шуток всех категорий
            url = 'https://api.chucknorris.io/jokes/random?category=' + i
            result = requests.get(url)
            check = result.json()  # ответ из запроса в виде json
            check_info_value = check.get('value')  # сохраняем значение ключа value
            print(check_info_value)
            print('Status code: ' + str(result.status_code))
            assert 200 == result.status_code
            print('Status code is successfull!')


categories = JokeFromCategory()
categories.get_categories()

first_joke = JokeFromCategory()
first_joke.get_joke_from_category()
