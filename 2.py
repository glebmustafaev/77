import random
r = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
a = [2, 3, 4, 5, 6, 7, 8, 9, 10]
b = random.choice(r)
print(b)
list_ = []
for i in (a):
    for j in (a):
        if b == i * j:
            list_.append(i)
            list_.append(j)
for k in (n):
    for m in (n):
        if b == k + m:
            list_.append(k)
            list_.append(m)
            break
print(list_)