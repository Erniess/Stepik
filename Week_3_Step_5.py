# Распространённые форматы текстовых файлов: CSV, JSON

import csv

# используя двойные ковычки в csv файле можно объединять значения
with open('example.csv') as f:
    reader = csv.reader(f, delimiter=",") # можем указать свой разделитель
    for row in reader:
        print(row)

# Запись данных в csv формат
students = [
    ["Greg", "Dean", 70, 80, 90, "Good job, Greg"], # При записи библиотека автоматически проставит
    # кавычки
    ["Wirt", "Wood", 80, 80.2, 80, "Nice done"]
]

with open('example.csv', 'a') as f:
    writer = csv.writer(f)
    for student in students:
        writer.writerow(student)

with open('example.csv', 'a') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL) # явно указать все помещать в кавычки
    writer.writerows(students)

# JSON
import json

student1 = {
    "first_name": "Greg",
    "last_name": "Dean",
    "certificate": True,
    "scores": [
      70,
      80,
      90
    ],
    "description": "Good job, Greg"
}
student2 = {
    "first_name": "Wirt",
    "last_name": "Wood",
    "certificate": True,
    "scores": [
      70,
      80,
      90
    ],
    "description": "Nicely Day"
}
data = [student1, student2]
print(json.dumps(data, indent=4, sort_keys=True)) # dumps Объект, количество отступов, сортировка
with open('example.json', 'w') as f:
    json.dump(data, f, indent=4, sort_keys=True) # dump Запись в файл

data_json = json.dumps(data, indent=4, sort_keys=True) # Перевод в формат json
data_again = json.loads(data_json) # Конвертация из формата json в python object
print(sum(data_again[0]['scores']))

with open('example.json', 'r') as f: # Чтение из файла json
    data_again = json.load(f)
    print(sum(data_again[0]['scores']))

