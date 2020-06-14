x, n = map(int, input().split())

if n != 0:
    p = list(map(int, input().split()))
else:
    print(x)
    exit()

dif = 100
ans = 0

for i in range(min(p) - 1, max(p) + 2):
    if not (i in p):
        if dif > abs(x - i):
            dif = abs(x - i)
            ans = i

print(ans)



