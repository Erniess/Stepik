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

arts_id = [
    '4d8b92b34eb68a1b2c0003f4',
    '537def3c139b21353f0006a6',
    '4e2ed576477cc70001006f99',
    '4d8b92b34eb68a1b2c0003f4',
    '537def3c139b21353f0006a6',
    '4e2ed576477cc70001006f99',
]
for art_id in arts_id:
    art_name_born = Artsy(art_id.rstrip())
    print(art_name_born[1], art_name_born[0])
    if art_name_born[1] not in artist_out: artist_out[art_name_born[1]] = [art_name_born[0]]
    else: artist_out[art_name_born[1]].append(art_name_born[0])

for art_year in sorted(artist_out):
    print(artist_out[art_year])
