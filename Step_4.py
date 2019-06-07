n = int(input())
db = {}

for i in range(n):
    args = input().split(' : ')
    for id, int_class in enumerate(args):
        if id == 0 and int_class not in db: db[int_class] = []
        else:
            for par_class in int_class.split(' '):
                if par_class not in db: db[par_class] = []
                if args[0] not in db[par_class]: db[par_class].append(args[0])
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start not in graph:
        return None
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

q = int(input())
for _ in range(q):
    args = input().split(' ')
    if len(args) > 1 and args[0] != args[1]: print('Yes' if find_path(db, args[0], args[1]) else 'No')
    else: print('Yes')