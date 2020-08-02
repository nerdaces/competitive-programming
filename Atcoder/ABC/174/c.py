k = int(input())

if k % 2 == 0:
    print('-1')
    exit()

s = 7
cnt = 1
while cnt <= 10**2:
    if s % k == 0:
        print(cnt)
        exit()
    s += 7 * 10**cnt
    cnt += 1

print(k-1)
exit()

# print('-1')