n = int(input())

if n==1:
    print(0)
elif n==2:
    print(2)
else:
    div = 10**9 + 7
    ans = n * (n-1)
    ans %= div
    while n>0:
        # ans *= n
        # ans %= div
        if n-2>0:
            ans *= 10
            ans %= div
        n -= 1
    print(ans)

