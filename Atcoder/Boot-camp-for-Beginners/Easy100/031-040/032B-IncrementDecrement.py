n = int(input())
s = input()

x = 0
maxV = x
for i in range(n):
    if s[i] == 'I':
        x += 1
        maxV = max(maxV, x)
    else:
        x -= 1

print(maxV)
