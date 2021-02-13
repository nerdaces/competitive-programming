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
        if b<0:
            if c>=2*b+1:
                cnt-=c-(2*b+1)+4*b
        else:
            if c>=2*b+2:
                cnt-=c-2*b
    print(cnt)