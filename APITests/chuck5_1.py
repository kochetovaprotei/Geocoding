import requests

url = 'https://api.chucknorris.io/jokes/random'
print(url)
result = requests.get(url)  # отправляем запрос апи
print('Status code: ' + str(result.status_code))  # запрашиваем статус код из ответа
assert 200 == result.status_code  # сравнимваем значение с выводимыми

result.encoding = 'utf-8' # чтобы формат ответа приводился к единому
print('Response: ' + result.text)  # текст тела ответа
