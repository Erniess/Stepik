# Вам дана частичная выборка из датасета зафиксированных преступлений,
# совершенных в городе Чикаго с 2001 года по настоящее время.
#
# Одним из атрибутов преступления является его тип – Primary Type.
#
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное
# число раз в 2015 году.

import csv
import re

attr = {}
pattern = r"\/(2015).*"

with open('Crimes.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if re.findall(pattern, row['Date']):
            if row['Primary Type'] in attr: attr[row['Primary Type']] += 1
            else: attr[row['Primary Type']] = 1
print(max(attr, key=attr.get))

