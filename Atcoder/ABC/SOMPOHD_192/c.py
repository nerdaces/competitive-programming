def cast(x):
    res = 0
    l = len(x)
    for i in x:
        res += int(i) * 10**(l-1)
        l-=1
    return res


n,k=map(int, input().split())

for i in range(k):
    n=str(n)
    x=sorted(n,reverse=True)
    y=sorted(n)
    n=cast(x)-cast(y)
print(n)
