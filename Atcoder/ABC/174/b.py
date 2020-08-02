n, d = map(int, input().split())

x, y = [0] * n, [0] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())

cnt = 0
for i in range(n):
    if pow(x[i]**2+y[i]**2, 0.5) <= d:
        cnt += 1

print(cnt)
