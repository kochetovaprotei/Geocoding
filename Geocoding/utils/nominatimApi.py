import requests


class NominatimApi:
    headers = {'Content-Type': 'application/json'}
    cookie = ""
    base_url = 'https://nominatim.openstreetmap.org/'
    format_json = '&format=jsonv2'

    """Метод отправки запроса"""

    def get_request(self, url):
        result = requests.get(url, headers=self.headers, cookies=self.cookie)
        result.encoding = 'utf-8'
        result_check_info_responce = result.json()
        print('Status code: ' + str(result.status_code))
        assert 200 == result.status_code
        print(f'Полный ответ из запроса по имени: {result_check_info_responce}')

        return result_check_info_responce

    """Метод прямого нахождения по имени"""

    # @staticmethod  # чтобы не привязываться к конкретному классу
    def search(self, query):
        filename = 'search.php?'
        search_url = NominatimApi.base_url + filename + str(query) + NominatimApi.format_json
        print(f'URL, который ищем:{search_url}')

        result = self.get_request(url=search_url)
        return result

    # NominatimApi.search(query='q=иорданский+пруд')

    """Метод обратного нахождения по координатам"""

    def reverse(self, query1, query2):
        filename = 'reverse.php?'
        reverse_url = NominatimApi.base_url + filename + 'lat=' + str(query1) + '&lon=' + str(query2) + \
                      NominatimApi.format_json
        print(f'URL, который ищем:{reverse_url}')

        result = self.get_request(url=reverse_url)
        return result

# NominatimApi.reverse(query1='59.99357575', query2='30.3362719762346')
