t=int(input())
for i in range(t):
    # res,cnt=0,0
    res=0
    l, r = map(int, input().split())
    # for c in range(l,r+1):
    #     cnt=(r-l)-c+1
    #     if cnt>0:
    #         res+=cnt
    temp=(r-l)-l+1
    if temp>0:
        res=temp*(temp+1)/2
    print(int(res))