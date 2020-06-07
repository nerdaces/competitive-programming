n = int(input())
d = list(map(int, input().split()))

d.sort()
nn = int(n / 2)
print(d[nn] - d[nn - 1])