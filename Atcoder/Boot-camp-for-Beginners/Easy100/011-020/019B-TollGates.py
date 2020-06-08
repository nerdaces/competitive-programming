n, m, x = map(int, input().split())
a = list(map(int, input().split()))
cost_0, cost_n = 0, 0

# if max(a) <= x or min(a) >= x:
#     print(0)
#     exit(1)

for i in range(1, x):
    if i in a:
        cost_0 += 1

for i in range(x + 1, n):
    if i in a:
        cost_n += 1

print(min(cost_0, cost_n))