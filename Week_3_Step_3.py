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

# метасимволы - используются в паттернах для обозначения определенных условий
# . ^ $ * + ? { } [ ] \ | ( )

pattern = r' english\?' # Симфол ? необходимо экранировать тк являетя метасимволом
string = 'Do you speak english?'
match = re.search(pattern, string)
print(match)

pattern = r'a[a-zA-Z]c'
string = 'aac'
match_object = re.findall(pattern, string)
print(match_object)

string = 'abc, acc, aac, adc, aGc, aZc'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_types = re.sub(pattern, "abc", string)
print(fixed_types)

pattern = r'a[^a-zA-Z]c'
string = 'aac'
match_object = re.findall(pattern, string)
print(match_object)

string = 'abc, a.c, aac, a-c, aGc, aZc'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_types = re.sub(pattern, "abc", string)
print(fixed_types)

pattern = r'ab*a'
string = 'aa, aba, abba'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

pattern = r'ab+a'
string = 'aa, aba, abba'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

pattern = r'ab?a'
string = 'aa, aba, abba'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

pattern = r'ab{2,4}a'
string = 'aa, aba, abba, abbbba, abbbbbba'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

pattern = r'a[ab]+?a'
string = 'abaaba'
print(re.findall(pattern, string))
print(re.match(pattern, string))

# группировка символов
pattern = r'((abc)|(test|text)*)'
string = 'testtext'
matched = re.match(pattern, string)
print(matched.groups())

pattern = r'((abc)|(test|text)*)'
string = 'abc'
matched = re.match(pattern, string)
print(matched.groups())

pattern = r'Hello (abc|test)'
string = 'Hello abc'
matched = re.match(pattern, string)
print(matched)
print(matched.group(0))
print(matched.group(1))

pattern = r'(\w+)-\1' # \1 - указывает что необходимо найти точно такую же группу которую уже нашли
string = 'test-test'
matched = re.match(pattern, string)
print(matched)

pattern = r'(\w+)-\1'
string = 'test-text'
matched = re.match(pattern, string)
print(matched)

pattern = r'(\w+)-\1'
string = 'test-test chow-chow'
matched = re.sub(pattern, r'\1', string)
print(matched)

pattern = r'((\w+)-\2)'
string = 'test-test chow-chow'
matched = re.findall(pattern, string)
print(matched)

x = re.match(r'(te)*?xt', 'TEXT', re.IGNORECASE | re.DEBUG)
print(x)