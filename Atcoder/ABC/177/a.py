import math
d, t, s = map(int, input().split())

if math.ceil(d / s) <= t:
    print('Yes')
else:
    print('No')