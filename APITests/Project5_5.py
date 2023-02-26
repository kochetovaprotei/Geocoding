import requests


class JokeFromCategory:
    """Создание шутки из категории"""
    def __init__(self):
        pass

    def get_joke_from_users_category(self):
        """Создание шутки из категории"""
        url = 'https://api.chucknorris.io/jokes/categories'
        result = requests.get(url)
        category = result.json()
        print('Categories: ' + result.text)
        print('Enter any category: \n')
        entered_category = input()
        if entered_category in category:
            url = 'https://api.chucknorris.io/jokes/random?category=' + entered_category
            result = requests.get(url)
            check = result.json()  # ответ из запроса в виде json
            check_info_value = check.get('value')  # сохраняем значение ключа value
            print(check_info_value)
            print(url)
            print('Status code: ' + str(result.status_code))
            assert 200 == result.status_code
            print('Status code is successfull!')
        else:
            print("Category doesn't exist! Try another one.")


first_joke = JokeFromCategory()
first_joke.get_joke_from_users_category()
