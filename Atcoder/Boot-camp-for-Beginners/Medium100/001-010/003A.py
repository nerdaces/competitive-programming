# wakaranakatta
s = input()

left = [0]*len(s)
cnt = 0
for i in range(len(s)):
    if s[i] == '<':
        cnt += 1
    left[i] = cnt

print(left)

right = [0]*len(s)
cnt = 0
for i in range(len(s)):
    if s[len(s)-1-i] == '>':
        cnt += 1
    right[len(s)-1-i] = cnt

print(right)

ans = 0
for i in range(len(s)):
    ans += max(left[i], right[i])

print(ans)
