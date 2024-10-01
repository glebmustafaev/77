import random
from itertools import count

r = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
a = [2, 3, 4, 5, 6, 7, 8, 9, 10]
b = random.choice(r)
list_ = []
for i in (a):
    for j in (a):
        if b == i * j:
            e = [i, j]
            e.sort()
            list_.append(e)

for k in (n):
    for m in (n):
        if b == k + m:
            z = [k, m]
            z.sort()
            list_.append(z)
new_list = (' '.join(map(str, list_)))

print(b, '-', new_list)

