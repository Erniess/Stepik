# Вам дается текстовый файл, содержащий некоторое количество непустых строк.
# На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

filename = 'dataset_24465_4.txt'
with open(filename) as f, open('newfile.txt', 'w') as out_file:
    out_file.write('\n'.join(reversed([i.rstrip() for i in f.readlines()])))


# Найти в данной в файловой структуре все директории, в которых есть хотя бы один файл с расширением ".py".
#
# Ответом на данную задачу будет являться файл со списком таких директорий,
# отсортированных в лексикографическом порядке.

import os

answer = []
for current_dir, dirs, files in os.walk('./main'):
    dir = 'main{}'.format(current_dir.split('.')[1])
    [answer.append(dir) for file in files if os.path.splitext(file)[1] == '.py' and dir not in answer]

with open('sample_answer.txt', 'w') as f:
    f.write('\n'.join(answer))