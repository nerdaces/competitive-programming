n, m = map(int, input().split())
l, r = [0]*(m+1), [0]*(m+1)
for i in range(m):
    l[i], r[i] = map(int, input().split())

res = [i+1 for i in range(n)]

for i in range(m):
    if min(res) < l[i]:
        for j in range(min(res), l[i]):
            if j in res:
                res.remove(j)
    if max(res) > r[i]:
        for j in range(r[i]+1, max(res)+1):
            if j in res:
                res.remove(j)

print(len(res))
