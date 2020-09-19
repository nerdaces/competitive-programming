n=int(input())
cnt=0
ans='No'
for i in range(n):
    x,y = map(int, input().split())
    if x==y:
        cnt+=1
        if cnt==3:
            ans='Yes'
    else:
        cnt=0
print(ans)
