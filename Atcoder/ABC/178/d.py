s = int(input())

if s < 3:
    print(0)
    exit()

cnt=1
if s%2==0:
    end=int(s/2)
else:
    end=int(s/2)+1

for i in range(3,end+1):
    j=s-i
    if j>=3:
        cnt+=1
        if j/2>0:
            