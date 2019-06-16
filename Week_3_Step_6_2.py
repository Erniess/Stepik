# В этой задаче вам необходимо воспользоваться API сайта artsy.net
#
# API проекта Artsy предоставляет информацию о некоторых деятелях искусства,
# их работах, выставках.
#
# В рамках данной задачи вам понадобятся сведения о деятелях искусства
# (назовем их, условно, художники).
#
# Вам даны идентификаторы художников в базе Artsy.
# Для каждого идентификатора получите информацию о имени художника и
# годе рождения.
# Выведите имена художников в порядке неубывания года рождения. В случае если
# у художников одинаковый год рождения, выведите их имена в лексикографическом
# порядке.
# Получить токен:
# client_id = '61b6255f3f63186f643d'
# client_secret = '3d47bef3f25b2373179d4e4567401382'

# def get_token(client_id, client_secret):
#     r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
#                   data={
#                       "client_id": client_id,
#                       "client_secret": client_secret
#                   })
#     j = json.loads(r.text)
#     token = j["token"]
#     return token
#
# token = get_token(client_id, client_secret)

import requests
import json
import sys

artist_out = {}

def Artsy(id, token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsImV4cCI6MTU2MTI4NTk4OCwiaWF0IjoxNTYwNjgxMTg4LCJhdWQiOiI1ZDA2MWFlNDEzYzBlMTAwMGU3NjIzYTgiLCJpc3MiOiJHcmF2aXR5IiwianRpIjoiNWQwNjFhZTRhN2NkNTIwMDExMDE3YTViIn0.6ZW6hT7xUgzTS6BSMoj7TiqNrsLVewNVbh-vDX_q8mE'):
    headers = {"X-Xapp-Token" : token}
    r = requests.get("https://api.artsy.net/api/artists/{}".format(id), headers=headers)
    j = json.loads(r.text)
    sortable_name = j["sortable_name"]
    birthday = j["birthday"]
    return sortable_name, birthday

for art_id in sys.stdin:
    art_name_born = Artsy(art_id.rstrip())
    if art_name_born[1] not in artist_out: artist_out[art_name_born[1]] = [art_name_born[0]]
    else: artist_out[art_name_born[1]].append(art_name_born[0])

for art_year in sorted(artist_out):
    [print(art_name) for art_name in sorted(artist_out[art_year])]
