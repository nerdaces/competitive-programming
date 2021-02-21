def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

k=int(input())

cnt=1
for a in range(2,k+1):
    cnt+=3
    div=make_divisors(a)
    if len(div)%2==0:
        cnt+=6*(len(div)/2-1)
    else:
        cnt+=6*(len(div)//2-1)
        cnt+=3
    if int(a**(1/3))**3==a:
        cnt+=1
        cnt-=3
    for i in div[1:-1]:
        if int(i**(1/2))**2==i:
            cnt+=3
print(int(cnt))