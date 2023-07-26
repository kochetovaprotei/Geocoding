import allure
import requests
from utils.logger import Logger
from utils.allure_logging import http_log


class NominatimApi:
    headers = {'Content-Type': 'application/json'}
    cookie = ""
    base_url = "https://nominatim.openstreetmap.org/"
    format_json = "&format=jsonv2"

    """Отправка запроса, проверки на статус-код"""

    @classmethod
    def get_request(cls, url):
        Logger.add_request(url, method="GET")
        with allure.step("Отправить запрос с тестовыми данными"):
            result = requests.get(url, headers=cls.headers, cookies=cls.cookie)
        Logger.add_response(result)
        result.encoding = 'utf-8'
        result_response = result.json()
        # allure.attach("name", "content")

        with allure.step("Проверить статус-код 200"):
            with allure.step("Проверить, есть ли ошибки при успешном статус-коде"):
                if result.status_code == 200:
                    http_log.info(f"Status code: {result.status_code}")
                    if not result_response:
                        raise Exception("200 ERROR:NO SEARCH RESULTS FOUND")
                    elif result_response == {"error": "Unable to geocode"}:
                        raise Exception("200 ERROR:Unable to geocode")
                elif result.status_code == 400:
                    raise Exception("400 Bad Request")
                elif result.status_code == 404:
                    raise Exception("404 Not found")
                elif result.status_code == 500:
                    raise Exception("500 Internal Server Error")
                elif result.status_code == 502:
                    raise Exception("502 Bad Gateway")
                elif result.status_code == 408:
                    raise Exception("408 Request Timeout")
        http_log.info(f"Полный ответ запроса:\n{result_response}")

        return result_response

    """Отправка запроса search по имени"""

    @classmethod
    def search(cls, query):
        search_url = f"{cls.base_url}search.php?{str(query)}{cls.format_json}"
        http_log.info(f"URL запроса по имени:\n{search_url}")
        result = cls.get_request(url=search_url)
        return result

    """Отправка запроса reverse по координатам"""

    @classmethod
    def reverse(cls, query1, query2):
        reverse_url = f"{cls.base_url}reverse.php?lat={str(query1)}&lon={str(query2)}{cls.format_json}"
        http_log.info(f"URL запроса по координатам:\n{reverse_url}")
        result = cls.get_request(url=reverse_url)
        return result
