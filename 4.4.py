# a = [6, 2, 4, 5, 0, 7, 2, 1, 9, 7, 7, 6, 1, 7]
# [4, 5, 0, 9]
# a = [6, 7, 4, 4, 2, 2, 8]
# [6, 7, 8]
# a = [5, 8, 2, 8, 5, 0, 9]
# [2, 0, 9]
n = len(a)
p = 0
b = []
for i in range(0, n):
        for k in range(0, n):
            if a[i] == a[k]:
                p += 1
        if p == 1:
            b.append(a[i])
        p = 0
print(b)