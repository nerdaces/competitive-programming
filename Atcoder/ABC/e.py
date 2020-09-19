n,x,m = map(int, input().split())

a=x
ans=a
for i in range(n):
    a=a**2%m
    ans+=a

print(ans)