# Рассмотрим два HTML-документа A и B.
# Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега.
# Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и из C в B можно перейти за один переход.
#
# Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
#
# Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

import requests
import re


url_a = input()
url_b = input()

def reqres(url):
    res = requests.get(url)
    return res.text

pattern = r'<a href="(.*)">|\/\?'
ans = 'No'
for list_url in re.findall(pattern, reqres(url_a)):
    if url_b in re.findall(pattern, reqres(list_url)): ans = 'Yes'
print(ans)

# Короткая запись
import re, requests

url_a, url_b, links = input(), input(), lambda url: re.findall( r'<a href="(.*)">|\/\?', requests.get(url).text)
print('Yes' if [1 for list_url in links(url_a) if url_b in links(list_url)] else 'No')