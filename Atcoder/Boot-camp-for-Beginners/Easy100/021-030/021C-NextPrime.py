def nextprime(v):
    for i in range(2, v):
        if v % i == 0:
            return False
    return True

x = int(input())

i = 0
while True:
    if nextprime(x+i):
        print(x+i)
        exit(0)
    i += 1

