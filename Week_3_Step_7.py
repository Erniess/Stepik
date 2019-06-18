# XML, библиотека ElementTree, библиотека lxml
from xml.etree import ElementTree

tree = ElementTree.parse("example.xml")
root = tree.getroot()
# use root = ElementTree.fromstring(string_xml_data) to parse from string

print(root)
print(root.tag, root.attrib)

for child in root:
    print(child.tag, child.attrib)

print(root[0][0].text) # индексация

for element in root.iter('scores'):
    print(element)
    score_sum = 0
    for child in element:
        score_sum += float(child.text)
    print(score_sum)

tree.write('example_copy.xml') # Создание и запись нового xml

greg = root[0]
module1 = next(greg.iter('module1'))
print(module1, module1.text)

module1.text = str(float(module1.text) + 30)

tree.write('example_modified.xml')

# Добавляем новый элемент
certificate = greg[2]
certificate.set('type', 'with distinction')

tree.write('example_modified.xml')

# Создаем новый элемент
description = ElementTree.Element('description')
description.text = 'Showed excellent skills during the course'
greg.append(description)
tree.write('example_modified.xml')

# найти элемент find
description = greg.find('description')

# Удалить элемент
greg.remove(description)
tree.write('example_modified.xml')

# Создание полного дерева
root = ElementTree.Element('student')

first_name = ElementTree.SubElement(root, 'firstName')
first_name.text = 'Greg'

second_name = ElementTree.SubElement(root, 'second_name')
second_name.text = 'Dean'

scores = ElementTree.SubElement(root, 'scores')

module1 = ElementTree.SubElement(scores, 'module1')
module1.text = '100'

module2 = ElementTree.SubElement(scores, 'module2')
module2.text = '80'

module3 = ElementTree.SubElement(scores, 'module3')
module3.text = '90'

tree = ElementTree.ElementTree(root)
tree.write('student.xml')

# LXML парсер
from lxml import etree
import requests

res = requests.get('https://docs.python.org/3/')
print(res.status_code)
print(res.headers['Content-Type'])

parser = etree.HTMLParser()
root = etree.fromstring(res.text, parser)

for element in root.iter('a'):
    print(element, element.attrib)