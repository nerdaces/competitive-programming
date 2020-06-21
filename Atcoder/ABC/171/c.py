n = int(input())

cnt = 26
l = 1
s = cnt
while s < n:
    l += 1
    s += cnt ** l

# print(l)

name = ['a'] * l
x = ord('a') - 1

for i in range(l):
    temp = int(n / cnt)
    # if temp == 0:
    #     name += 'z'
    # else:
    #     name += chr(x + temp)
    name[i] = chr(ord(name[i]) + temp)
    l -= 1
    n -= cnt ** l

print(name)


