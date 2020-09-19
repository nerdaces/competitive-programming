n=int(input())
cnt=0

if n%2==0:
    end=int(n/2)
else:
    end=int(n/2)+1

for b in range(1,end):
    for c in range(1,n-b):
        if (n-c)%b==0:
            cnt+=1

print((cnt-1)*2+1)