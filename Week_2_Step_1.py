

class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0

class MyList(list, EvenLengthMixin):
    pass

ml = MyList([1, 12, 4, 17, 3])
ml.sort()
print(ml)

# Вашей программе будет доступна функция foo, которая может бросать исключения.
#
# Вам необходимо написать код, который запускает эту функцию, затем ловит
# исключения ArithmeticError, AssertionError, ZeroDivisionError и выводит
# имя пойманного исключения.

try:
    1/0
except ZeroDivisionError:
    print('ZeroDivisionError')
except ArithmeticError:
    print('ArithmeticError')
except AssertionError:
    print('AssertionError')

# Вам дано описание наследования классов исключений в следующем формате.
# <имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
# Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.

n = int(input())
p_excep = {}
for i in range(n):
    args = input().split(' : ')
    for id, cond in enumerate(args):
        if id == 0:
            if cond not in p_excep: p_excep[cond] = []
            else: continue
        else:
            for p_cond in cond.split(' '):
                if p_cond not in p_excep: p_excep[p_cond] = []
                if p_cond not in p_excep[args[0]]: p_excep[args[0]].append(p_cond)


def tree(graph, start):
    newpath = []
    for node in graph[start]:
        newpath.append(node)
        if node in graph:
            newpath = newpath + tree(graph, node)
    return newpath


q = int(input())
viewed = []
for _ in range(q):
    args = input()
    parents = tree(p_excep, args)
    if args not in viewed:
        if [x for x in parents if x in viewed]: print(args)
        viewed.append(args)

