b,c=map(int,input().split())
cnt=1

if b==0:
    if c>=2:
        cnt+=c-1
    print(cnt)
    exit()
else:
    if c==1:
        cnt+=1
    elif c==2:
        cnt+=2
    else:
        cnt+=2*(c-1)
        # if 2*b+1>=c:
        #     cnt-=1
        cnt-=max(0,min(b+(c-2)//2, -b+(c-1)//2)-max(b-c//2, -b-(c-1)//2)+1)
    print(cnt)