s = int(input())

i = 1
while True:
    if s == 4 or s == 2 or s == 1:
        print(i+3)
        exit(0)
    if s % 2 == 0:
        s /= 2
    else:
        s = 3 * s + 1
    i += 1

