# Вывести повторы в списске
objects = [1, 2, 1, 2, 3]
ans = 0
tmp = []
for obj in objects:
    if obj not in tmp:
        tmp.append(obj)
        ans += 1
print(len(set(id(i) for i in objects)))