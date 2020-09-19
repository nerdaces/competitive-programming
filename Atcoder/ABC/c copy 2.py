n=int(input())
cnt=0

for b in range(1,n):
    cnt+=int((n-1)/b)

print(cnt)