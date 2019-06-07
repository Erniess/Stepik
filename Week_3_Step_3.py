# Регулярные выражения в Python
x = 'Hello\"world' # Экранируем символ " обратным слешем \
print(x)

x = r'Hello\"world' # Чтобы все символы в строке не экранировать ставим r в начале
print(x)

import re

print(re.match)
print(re.search)
print(re.findall)
print(re.sub)

pattern = r'abc'
string = 'abc'
match_object = re.match(pattern, string)
print(match_object)

pattern = r'abc'
string = 'babc'
match_object = re.match(pattern, string)
print(match_object)

# span=(1, 4) - значит: 0b1a2b3c4 искомое значение найдено в диапазоне между символами 1 и 4
pattern = r'abc'
string = 'babc'
match_object = re.search(pattern, string)
print(match_object)

# [] - множество условий в шаблоне
pattern = r'a[abc]c'
string = 'aac'
match_object = re.match(pattern, string)
print(match_object)
string = 'aacc'
match_object = re.match(pattern, string)
print(match_object)

pattern = r'a[abc]c'
string = 'abc, acc, aac'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_types = re.sub(pattern, "abc", string) # Ищет все вхождения по шаблону и заменяет их на abc
print(fixed_types)