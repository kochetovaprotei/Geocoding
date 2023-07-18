import requests
from utils.logger import Logger

class NominatimApi:
    headers = {'Content-Type': 'application/json'}
    cookie = ""
    base_url = 'https://nominatim.openstreetmap.org/'
    format_json = '&format=jsonv2'

    """Метод отправки запроса"""

    def get_request(self, url):
        # with allure.step("GET"):
        Logger.add_request(url, method="GET")
        result = requests.get(url, headers=self.headers, cookies=self.cookie)
        Logger.add_response(result)
        result.encoding = 'utf-8'
        result_check_info_response = result.json()

        if result.status_code == 200:
            print('Status code: 200 OK')
        else:
            print(f'STATUS CODE: {str(result.status_code)}')

        if not result_check_info_response:
            print("NO SEARCH RESULTS FOUND")
        elif result_check_info_response == {"error": "Unable to geocode"}:
            print("ERROR-MESSAGE:Unable to geocode")
        elif result_check_info_response == {"error": {"code": 400, "message":"Floating-point number expected for "
                                                                             "parameter 'lat'"}}:
            print("ERROR-MESSAGE:Floating-point number expected for parameter 'lat'")
        else:
            print(f'Полный ответ из запроса по имени: {result_check_info_response}')

        return result_check_info_response

    """Метод прямого нахождения по имени"""


    def search(self, query):
        search_url = NominatimApi.base_url + 'search.php?' + str(query) + NominatimApi.format_json
        print(f'URL, который ищем:{search_url}')
        result = self.get_request(url=search_url)
        return result

    # NominatimApi.search(query='q=иорданский+пруд')

    """Метод обратного нахождения по координатам"""

    def reverse(self, query1, query2):
        reverse_url = NominatimApi.base_url + 'reverse.php?lat=' + str(query1) + '&lon=' + str(query2) + \
                      NominatimApi.format_json
        print(f'URL, который ищем:{reverse_url}')
        result = self.get_request(url=reverse_url)
        return result

# NominatimApi.reverse(query1='59.99357575', query2='30.3362719762346')
