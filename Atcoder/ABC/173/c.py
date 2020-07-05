import itertools
import math

h,w,k = map(int, input().split())

c = [0]*h
for i in range(h):
    c[i] = input()

ans = 0
ch, cw = [0]*(h+1), [0]*(w+1)
for i in range(h):
    for j in range(w):
        if c[i][j] == '#':
            ch[i+1] += 1
            cw[j+1] += 1

# print(ch, cw)

all = sum(ch)
if all < k:
    print(0)
    exit()

# l = [0,1,2,3,4,5]
# p = itertools.permutations(l)
# print(p)

# for i in range(h+1):
#     for j in range(w+1):
#         temp = all - ch[i] - cw[j]
#         if c[i-1][j-1] == '#':
#             temp -= 1
#         if temp == k:
#             ans += 1

# print(ans)

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def combinations_with_replacement_count(n, r):
    return combinations_count(n + r - 1, r)



print(combinations_count(all, k))