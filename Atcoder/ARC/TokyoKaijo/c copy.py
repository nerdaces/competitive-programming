# i was on my way to improve complexity
import math

n, k = map(int, input().split())
a = list(map(int, input().split()))

a.insert(0, 0)

# for i in range(k):
#     ans = [1] * (n + 1)
#     for j in range(1, n + 1):
#         if a[j] > 0:
#             x = math.ceil(j - a[j] - 0.5)
#             y = math.floor(j + a[j] + 0.5)
#             for t in range(max(x, 1), min(y + 1, n + 1)):
#                 if t != j:
#                     ans[t] += 1
#     a = ans

for i in range(k):
    ans = [1] * (n + 1)
    bt = [0] * (n + 1)
    up = [0] * (n + 1)
    for j in range(1, n + 1):
        if a[j] > 0:
            bt[j] = math.ceil(j - a[j] - 0.5)
            up[j] = math.floor(j + a[j] + 0.5)



a = [str(s) for s in a]
a = ' '.join(a)
print(a[2:])