import math

n, k = map(int, input().split())
a = list(map(int, input().split()))

af = [float(a[i]) for i in range(n)]

s = sum(a)
# a.sort()
# a.reverse()

for i in range(n):
    t = round(k * a[i] / s)
    k -= t
    temp = a[i]
    af[i] = a[i] / (t + 1)
    s -= temp + af[i]
    print(s)

print(math.ceil(max(af)))
