an, bn, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

x, y, c = [0] * m, [0] * m, [0] * m
for i in range(m):
    x[i], y[i], c[i] = map(int, input().split())

min_cost = x[0] + y[0]
for i in range(an):
    for j in range(bn):
        sum = a[i] + b[j]
        if (i in x) and (j in y):
            if x.index(i) == y.index(j):
                sum -= 
        min_cost = min(min_cost, sum)

print(min_cost)
