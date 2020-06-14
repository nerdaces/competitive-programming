x, y = map(int, input().split())

for a in range(x + 1):
    tem = 2 * a + 4 * (x - a)
    if (tem == y):
        #  and (2 * x <= y <= 4 * x):
        print('Yes')
        exit()

print('No')