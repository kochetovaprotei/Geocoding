import requests

"""Список HTTP методов"""


class HttpMethods:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod  # чтобы не привязываться к конкретному классу
    def search_and_reverse(url):
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result
