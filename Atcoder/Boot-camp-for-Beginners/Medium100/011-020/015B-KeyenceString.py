s = input()
q = 'keyence'

j, cnt = 0, 0
flag = False
for i in range(len(s)):
    if s[i] == q[j]:
        j += 1
        if flag:
            cnt += 1
        if j == len(q) - 1:
            break
        flag = False
    else:
        flag = True

if i < len(s)-1:
    cnt += 1

if j == len(q)-1 and cnt <= 1:
    print('YES')
else:
    print('NO')