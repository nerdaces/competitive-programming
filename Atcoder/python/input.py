# a (str)
a = input()

# a (int)
a = int(input())

# s1 s2 (str)
s = input().split()

# n x
n, x = map(int, input().split())

# s1 s2 (int)
s = list(map(int, input().split()))

# a b (int)
a, b = list(map(int, input().split()))

# s1
# s2
# s3 (int) 
s = [int(input()) for i in range(3)]

# x1 y1 c1
# ...
# xm ym cm
x, y, c = [0] * m, [0] * m, [0] * m
for i in range(m):
    x[i], y[i], c[i] = map(int, input().split())

# complex input
import sys
f = sys.stdin # file style
a = f.readline() # read 1 line
aa = a.strip('\n')

