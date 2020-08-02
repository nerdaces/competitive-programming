import math

n, k = map(int, input().split())
a = list(map(int, input().split()))

s = sum(a)
t = [0]*n

for i in range(n):
    t[i] = round(k * a[i] / s)

for i in range(n):
    a[i] = math.ceil(a[i] / (t[i] + 1))

print(max(a))
