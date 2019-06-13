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