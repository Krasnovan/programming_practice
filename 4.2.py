# a = [1, 2, 3, 4, 7, 5]
#     [7, 2, 3, 4, 1, 5]
# a = [6, 2, 4, 5, 0, 7, 2, 1]
#     [6, 2, 4, 5, 7, 0, 2, 1]
# a = [5, 4, 3, 2, 1]
#     [1, 4, 3, 2, 5]
b = []
m1 = min(a)
m2 = max(a)
n = len(a)
for i in range(0, n):
    if a[i] == m1:
        n1 = i
    if a[i] == m2:
        n2 = i
for i in range(0, n):
    if i == n1:
        b.append(m2)
    elif i == n2:
        b.append(m1)
    else:
        b.append(a[i])
print(b)


