A, B = list(map(int, input().split()))
count = 1
i = 0

while count < B:
    count +=  A - 1
    i += 1

print(i)