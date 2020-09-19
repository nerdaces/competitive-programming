n=int(input())
cnt=0
for b in range(1,n):
    for c in range(1,n):
        if (n-c)%b==0:
            cnt+=1
            # print(b,c)
        elif (n-c)/b<1:
            break
print(cnt)
# print((cnt-1)*2+1)
# int(n/2)+1