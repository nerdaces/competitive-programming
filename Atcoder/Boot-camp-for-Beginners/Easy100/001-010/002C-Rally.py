N = int(input())
X = list(map(int, input().split()))
ave = round(sum(X) / N)
ans = 0

for i in range(N):
    ans += (X[i] - ave) ** 2

print(ans)


