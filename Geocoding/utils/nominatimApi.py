import allure
import requests
from utils.logger import Logger
from utils.allure_logging import http_log
import logging


class NominatimApi:
    headers = {'Content-Type': 'application/json'}
    cookie = ""
    base_url = 'https://nominatim.openstreetmap.org/'
    format_json = '&format=jsonv2'

    """Метод отправки запроса"""

    def get_request(self, url):
        with allure.step("GET"):
            Logger.add_request(url, method="GET")
            result = requests.get(url, headers=self.headers, cookies=self.cookie)
            Logger.add_response(result)
            result.encoding = 'utf-8'
            result_check_info_response = result.json()
            allure.attach("name", "content")

            if result.status_code == 200:
                print('Status code: 200 OK')
            elif result.status_code == 400:
                raise Exception("400 Bad Request")
            elif result.status_code == 404:
                raise Exception("404 Not found")
            elif result.status_code == 500:
                raise Exception('500 Internal Server Error')
            elif result.status_code == 502:
                raise Exception('502 Bad Gateway')
            elif result.status_code == 408:
                raise Exception('408 Request Timeout')

            if not result_check_info_response:
                raise Exception('200 NO SEARCH RESULTS FOUND')
            elif result_check_info_response == {"error": "Unable to geocode"}:
                raise Exception("200 ERROR-MESSAGE:Unable to geocode")

            http_log.info(f'Полный ответ из запроса по имени: {result_check_info_response}')

            return result_check_info_response

    """Метод прямого нахождения по имени"""

    def search(self, query):
        search_url = NominatimApi.base_url + 'search.php?' + str(query) + NominatimApi.format_json
        print(f'URL, который ищем:{search_url}')
        result = self.get_request(url=search_url)
        return result

    """Метод обратного нахождения по координатам"""

    def reverse(self, query1, query2):
        reverse_url = NominatimApi.base_url + 'reverse.php?lat=' + str(query1) + '&lon=' + str(query2) + \
                      NominatimApi.format_json
        print(f'URL, который ищем:{reverse_url}')
        result = self.get_request(url=reverse_url)
        return result
