n = int(input())

a = n % 1000

if a == 0:
    print(0)
else:
    print(1000-a)