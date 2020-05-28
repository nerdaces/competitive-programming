n = int(input())
c = 0
max_c = 0
max_num = 1

for i in range(1, n+1):
    if i % 2 == 0:
        j = i
        c = 1
        j /= 2
        while j % 2 == 0:
            c += 1
            j /= 2
    if c > max_c:
        max_c = c
        max_num = i

print(max_num)

# cnt = 0
# while N > 1:
#     N = N//2
#     cnt +=1
# print(2**cnt)
