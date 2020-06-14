n = int(input())
a = list(map(int, input().split()))
cnt = 1

a.sort()
if a[0] == a[1]:
    cnt = 0

for i in range(1, n):
    if a.count(a[i]) >= 2:
        break
    for j in range(i):
        if a[j] > a[i] / 2:
            cnt += 1
            break
        if a[i] % a[j] == 0:
            break
        if j == i - 1:
            cnt += 1

print(cnt)