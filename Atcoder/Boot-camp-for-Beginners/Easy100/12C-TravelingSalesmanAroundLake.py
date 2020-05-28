k, n = map(int, input().split())
a = list(map(int, input().split()))
d = 0

for i in range(n-1):
    d = max(d, a[i+1] - a[i])
d = max(d, k - a[-1] + a[0])

print(k - d)