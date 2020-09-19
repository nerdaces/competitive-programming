n, m = map(int, input().split())
ans = 0
f = [[0]*n]*n

for i in range(m):
    a, b = map(int, input().split())
    if a > b:
        temp = b
        b = a
        a = temp
    if f[a] == 0:
        f[a] = tuple(f[a])
        f[a].insert(b)
        ans = max(ans, 1)
    else:
        f[a].insert(b)
        ans = max(ans, len(f[a])-1)

print(ans)


