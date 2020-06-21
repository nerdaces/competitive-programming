import collections

n = int(input())
a = list(map(int, input().split()))
q = int(input())

b, c = [0] * q, [0] * q
for i in range(q):
    b[i], c[i] = map(int, input().split())

a.sort()

# for i in range(q):
#     if b[i] in a:
#         s = a.index(b[i])
#         while s < n and a[s] == b[i]:
#             a[s] = c[i]
#             s += 1
#     print(sum(a))

sum = sum(a)
x = [0] * (max(c) + 1)

col = collections.Counter(a)
# print(col)

for i in range(q):
    cnt = 0
    if (b[i] in a) or x[b[i]] != 0:
        # cnt = a.count(b[i])
        cnt = col[b[i]]
        sum += (cnt + x[b[i]]) * (c[i] - b[i])
        x[c[i]] += cnt
    print(sum)