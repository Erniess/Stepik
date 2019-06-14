# В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
#
# Вам дается набор чисел. Для каждого из чисел необходимо узнать,
# существует ли интересный математический факт об этом числе.
#
# Для каждого числа выведите Interesting, если для числа существует
# интересный факт, и Boring иначе.
# Выводите информацию об интересности чисел в таком же порядке, в каком
# следуют числа во входном файле.
#
# Пример запроса к интересному числу:
# http://numbersapi.com/31/math?json=true
#
# Пример запроса к скучному числу:
# http://numbersapi.com/999/math?json=true


import requests

def _main():
    filename = 'dataset_24476_3.txt'
    url = 'http://numbersapi.com/'
    str = ''
    with open(filename, 'r')  as f:
        numbers = f.read().split()
        for num in numbers:
            if requests.get(url+num+'/math', params='json').json()['found']:
                str += 'Interesting\n'
            else:
                str += 'Boring\n'
    with open('dataset_ans.txt', 'w') as f:
        f.write(str)

if __name__ == '__main__':
    _main()