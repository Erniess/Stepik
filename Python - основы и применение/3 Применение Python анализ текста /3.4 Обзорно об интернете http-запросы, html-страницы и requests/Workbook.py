 # Обзорно об интернете: http-запросы, html-страницы и requests

import requests

# Получение заголовков и статуса
res = requests.get('https://docs.python.org/3.5/')
print(res.status_code)
print(res.headers['Content-Type'])

# Получение содержимого
print(res.content)
print(res.text)

res = requests.get('https://docs.python.org/3.5/_static/py.png')
print(res.status_code)
print(res.headers['Content-Type'])

print(res.content)
print(res.text)

# Получение содержимого в файл
with open('python.png', 'wb') as f:
    f.write(res.content)

# Параметры запроса url?ключ_запроса=значение

res = requests.get('https://yandex.ru/search/', params={'text': 'Stepic'})
print(res.status_code)
print(res.headers['Content-Type'])
print(res.url)
print(res.text)

res = requests.get('https://yandex.ru/search/',
                   params={
                       'text': 'Stepic',
                       'test': 'test1',
                       'name': 'Name With Spaces',
                       'list': ["test1", "test2"]
                   })
print(res.status_code)
print(res.headers['Content-Type'])
print(res.url)