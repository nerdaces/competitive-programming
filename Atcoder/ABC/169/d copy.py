n = int(input())
z = [2]
cnt = 2
flag = True

for i in range(3, n + 1):
    flag = True
    cnt = 2
    for j in z:
        if i % j == 0:
            flag = False
            while i >= j:
                if i == j ** cnt:
                    flag = True
                    break
                j += 1
            break
    if flag == True:
        z.append(i)

cnt = 0
p = 0
while n != 1:
    for i in range(p, len(z)):
        if n % z[i] == 0:
            n /= z[i]
            p = i + 1
            cnt += 1

print(cnt)
