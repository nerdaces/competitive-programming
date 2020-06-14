def minimum(a, b):
    mini = max(a)
    for i in b:
        k = b.index(i)
        maxi = a[k[0]]
        for j in k:
            maxi = max(maxi, a[j])
        mini = min(mini, maxi)

n, q = map(int, input().split())

a, b = [0] * n, [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())

c, d = [0] * n, [0] * n
for i in range(q):
    c[i], d[i] = map(int, input().split())

for i in range(q):
    b[c[i]] = d[i]
    print(minimum(a, b))


