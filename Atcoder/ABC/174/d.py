n = int(input())
c = input()

r = 0
for i in range(n):
    if c[i] == 'R':
        r += 1

ans = 0
for i in range(r, n):
    if c[i] == 'R':
        ans += 1

print(ans)
