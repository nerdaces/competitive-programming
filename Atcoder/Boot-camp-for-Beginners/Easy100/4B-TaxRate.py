import math

N = int(input())

a = math.floor(N / 1.08)
b = a + 1

aa = math.floor(a * 1.08)
bb = math.floor(b * 1.08)

if(aa == N):
    print(a)
else:
    if(bb == N):
        print(b)
    else:
        print(":(")