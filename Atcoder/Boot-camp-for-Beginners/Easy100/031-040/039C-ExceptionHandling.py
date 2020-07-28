# wa*4
n = int(input())
a = [int(input()) for _ in range(n)]

if n == 2:
    print(a[1])
    print(a[0])
    exit()

first, second = 0, 0
for i in range(1, n):
    if a[i] >= second:
        if a[0] >= first:
            second = first
            first = a[i]
        else:
            second = a[i]

print(first)

if a[0] >= second:
    if a[0] >= first:
        second = first
        first = a[0]
    else:
        second = a[0]

for i in range(1, n):
    if first == a[i]:
        print(second)
    else:
        print(first)


