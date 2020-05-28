n = int(input())
a = list(map(int, input().split()))
sum_a, sum_b = 0, 0

for i in range(n):
    sum_a += max(a)
    a[a.index(max(a))] = 0
    sum_b += max(a)
    a[a.index(max(a))] = 0

print(sum_a - sum_b)