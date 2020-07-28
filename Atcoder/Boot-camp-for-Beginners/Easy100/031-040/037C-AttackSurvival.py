n, k, q = map(int, input().split())
a = [int(input()) for _ in range(q)]

cnt = [0] * n

for i in a:
    cnt[i - 1] += 1

for c in cnt:
    if k - (q - c) > 0:
        print('Yes')
    else:
        print('No')

