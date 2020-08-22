h, w = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())
s = [0]*h
for i in range(h):
    s[i] = input()

x,y = 0,1
now = [ch, cw]
while True:
    if now[x] <= dh:
        exit()