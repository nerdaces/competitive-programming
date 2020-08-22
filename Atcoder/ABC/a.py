n, x, t = map(int, input().split())

temp = int(n / x)
if n % x != 0:
    temp += 1

print(t * temp)