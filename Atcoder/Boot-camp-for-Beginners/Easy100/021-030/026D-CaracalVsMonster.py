import math

h = int(input())

t = 1
e = 1
while h > 1:
    h = math.floor(h / 2)
    e *= 2
    t += e

print(t)

