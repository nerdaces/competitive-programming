h,w,k = map(int, input().split())
s = [input() for _ in range(h)]
ans =0

for ib in range(1<<h):
    for jb in range(1<<w):
        cnt = 0
        for i in range(h):
            for j in range(w):
                if ib>>i&1: continue
                if jb>>j&1: continue
                if s[i][j] == '#':
                    cnt+=1
        if cnt == k:
            ans += 1

print(ans)