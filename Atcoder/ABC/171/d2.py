n = int(input())
a = list(map(int, input().split()))
q = int(input())

b, c = [0] * q, [0] * q
for i in range(q):
    b[i], c[i] = map(int, input().split())

cnt = [0] * (10**5 +  5)
for i in range(n):
    cnt[a[i]] += 1

tot = sum(a)

for i in range(q):
    if cnt[b[i]] > 0:
        tot += cnt[b[i]] * (c[i] - b[i])
        cnt[c[i]] += cnt[b[i]]
        cnt[b[i]] = 0
    print(tot)

