# Одно из применений множественного наследование – расширение функциональности класса
# каким-то заранее определенным способом. Например, если нам понадобится логировать
# какую-то информацию при обращении к методам класса.

import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, arg):
        self.log(arg)
        super().append(arg)

a = LoggableList()
a.append('msg 1')
a.append('msg 2')
print(a)