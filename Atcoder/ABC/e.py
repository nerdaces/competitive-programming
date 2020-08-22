import collections

H, W, M = map(int, input().split())

h, w = [0]*M, [0]*M
for i in range(M):
    h[i], w[i] = map(int, input().split())

counter = collections.Counter(h)
h_max = max(counter.values())
mode_h = [key for key , value in counter.items() if value == h_max]
counter = collections.Counter(w)
w_max = max(counter.values())
mode_w = [key for key , value in counter.items() if value == w_max]

ans = 0
for i in mode_h:
    for j in mode_w:
        if ans < h.count(i) + w.count(j):
            ans = h.count(i) + w.count(j)
            for k in range(M):
                if h[k] == i and w[k] == j:
                    ans -= 1
            if ans == H + W - 1 or ans == M:
                print(ans)
                exit()

print(ans)

