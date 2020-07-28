# wa
s = input()

sl = [int(s[i]) for i in range(len(s))]
ans1 = [i%2 for i in range(len(s))]
ans2 = [i%2+1 for i in range(len(s))]

diff1, diff2 = 0, 0
for i in range(len(sl)):
    if sl[i] != ans1[i]:
        diff1 += 1
    if sl[i] != ans2[i]:
        diff2 += 1

print(min(diff1, diff2))
