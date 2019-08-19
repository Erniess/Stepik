# В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
# Во второй строке дано одно число days -- число дней.
#
# Вычислите и выведите год, месяц и день даты, которая наступит,
# когда с момента исходной даты date пройдет число дней, равное days.
# Ввод:
# 2015 12 31
# 1
# Вывод:
# 2016 1 1

import datetime

# Expl 1
new_date = datetime.date(*map(int, "2015 12 31".split())) + datetime.timedelta(days=int(1))
print(new_date.year, new_date.month, new_date.day)

# Expl 2
year, month, day = input().split()
day_delta = int(input())
new_date = datetime.date(int(year), int(month), int(day)) + datetime.timedelta(days=day_delta)
print(new_date.year, new_date.month, new_date.day)