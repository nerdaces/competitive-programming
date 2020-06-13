# correct
a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

aa = v * t
bb = w * t

if aa - bb >= abs(b - a):
    print('YES')
else:
    print('NO')