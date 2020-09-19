n,k = map(int, input().split())
div=998244353
# l,r = [0] * k, [0] * k
# for i in range(k):
#     l[i],r[i]=map(int, input().split())
s=[]
for i in range(k):
    l,r=map(int, input().split())
    s.append(l)
    s.append(r)
s=list(set(s))

cnt=0
i=0
sum_s=1
l=[]
while i<len(s):
    while sum_s<n:
        sum_s+=s[i]
        l.append(s[i])
        if sum_s==n:
            cnt+=1
            break
    if sum_s!=n:
        sum_s-=l[0]
        l=l[1:]
    else:
        i=0
        sum_s=1
        
print(cnt%div)