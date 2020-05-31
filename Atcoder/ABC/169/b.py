n = int(input())
a = list(map(int, input().split()))
ans = a[0]

if 0 in a:
    ans = 0
else:
    for i in range(1, n):
        if ans <= 10 ** 18:
            ans *= a[i]
        else:
            break

if ans <= 10 ** 18:
    print(ans)
else:
    print(-1)