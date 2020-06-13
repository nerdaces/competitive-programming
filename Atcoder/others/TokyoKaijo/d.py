# on my way to solve it
n = int(input())
vl, w = [0] * n, [0] * n
for i in range(n):
    vl[i], w[i] = map(int, input().split())
q = int(input())
vs, l = [0] * q, [0] * q
for i in range(q):
    vs[i], l[i] = map(int, input().split())

vl.insert(0, 0)
w.insert(0, 0)

dp = [[0] * n] * n

for i in range(q):
    # sum_w = 0
    # sum_v = 0
    for j in range(vs[i], 0):
        for k in range(l[j] + 1):
            if w[j] <= l[j]:
                dp[j + 1][k] = max(dp[j][l - w[j]] + vl[j], dp[j][k])
            else:
                dp[j + 1][k] = dp[j][k]
    print(dp[vs[i]][l[i]])
        # if sum_w + w[j] <= l[j]:
        #     sum_w += w[j]
        #     sum_v += vl[j]
    



