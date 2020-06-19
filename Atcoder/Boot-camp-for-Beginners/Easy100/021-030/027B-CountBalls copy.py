n, a, b = map(int, input().split())

x = []
cnt = 0
flag = True
while cnt < n:
    if flag:
        for j in range(a):
            if cnt + j >= n:
                break
            x.append(1)
        cnt += a
        flag = False
    else:
        for j in range(b):
            if cnt + j >= n:
                break
            x.append(0)
        cnt += b
        flag = True

cnt = 0
for i in range(n):
    if x[i] == 1:
        cnt += 1

print(cnt)
