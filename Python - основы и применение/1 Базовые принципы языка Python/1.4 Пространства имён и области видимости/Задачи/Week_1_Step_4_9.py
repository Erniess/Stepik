# Эмуляция пространства имен
""" Sample Input:

9
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar b
"""

n = int(input())
db = {'global' : {'parent' : None, 'vars' : []}}

def get(namesp, arg):
    return namesp if arg in db[namesp]['vars'] else get(db[namesp]['parent'], arg) if db[namesp]['parent'] else None


for i in range(n):
    cmd, namesp, arg = input().split()
    if cmd == 'add': db[namesp]['vars'].append(arg)
    elif cmd == 'create': db[namesp] = {'parent' : arg, 'vars' : []}
    elif cmd == 'get': print(get(namesp, arg))