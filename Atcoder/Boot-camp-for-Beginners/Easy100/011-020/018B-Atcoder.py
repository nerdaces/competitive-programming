s = input()

cnt = 0
max_cnt = 0

for i in range(len(s)):
    if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
        j = i
        cnt = 0
        while j < len(s) and (s[j] == 'A' or s[j] == 'C' or s[j] == 'G' or s[j] == 'T'):
            cnt += 1
            j += 1
        max_cnt = max(max_cnt, cnt)

print(max_cnt)