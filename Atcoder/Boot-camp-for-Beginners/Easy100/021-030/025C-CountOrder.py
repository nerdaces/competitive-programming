from itertools import permutations

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

for i, x in enumerate(permutations([i+1 for i in range(n)])):
    if x == p:
        a = i
    if x == q:
        b = i
print(abs(a-b))


