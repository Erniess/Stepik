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