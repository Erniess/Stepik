# Вашей программе на вход подается ссылка на HTML файл.
# Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов, на которые есть ссылка.
#
# Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов, которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть, за исключением случаев с относительными ссылками вида
# <a href="../some_path/index.html">.
#
# Сайты следует выводить в алфавитном порядке.\

import requests
import re

# Задаем шаблон определяющий ссылки на
# <a - где-то в строке есть место, которое нажинается с этих двух символов
# .*  - 0 или более любых символов (это отлавливает другие атрибуты нашего тега 'a'
# которые идут перед href.
# href= - собственно, атрибут href=
# [\'\"] - одинарная или двойная кавычки
# (?:.{3,5}://)? - ищем что-то похожее на http://, https://, ftp://  или вообще ничего
# ((?:[^\./]).*?) - группируем и ищем часть не начинающаяся на . или /
# (?:[/\:\'\"]) - отсекаем у группы хвосты, символы: / : ' "

pattern = r'<a.*href=[\"\'](?:.{3,5}://)?((?:[^\./]).*?)(?:[/\:\'\"])'
#res = requests.get(input()).text

# Тестовые запросы
res = """
<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">
<a href="http://redir.rbc.ru/cgi-bin/redirect.cgi?http://hc.ru/ru/">
<a href="gogo-it@mail.ru"
<link href="http://pics.rbc.ru/img/skin/fp_v3/layout_34.css"; rel="stylesheet" type=text/css>
<a target="_top" href="http://banner.rbc.ru/banredir.cgi?lid=firstpage_spec"; empty="true" style="display:none"></a>
<h4 class="lightGreen mBottom4"><a href="http://www.nashidengi.ru">"Наши деньги"</a></h4>
<a href="/users/79/def" class="top-link ember-link">
<a site=? href=s-http://www1.work.site.com/def#!-/cgi?=12:8080
<a href='https://www-abc.com.uk:443'
<a ver-m_n=1 href="smb://192.168.1.1/file"</a>
<a role="button" class="toggle link link_style"></a>
<a link rel="icon" sizes="32x32" href="/static/icon32.png?v=59">
"""
print(re.findall(pattern, res))

[print(url) for url in sorted(set(re.findall(pattern, res))) if '@' not in url]
