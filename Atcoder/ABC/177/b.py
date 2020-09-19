s = input()
t = input()

minc = len(t)
for i in range(len(s)-len(t)+1):
    c = 0
    for j in range(len(t)):
        if s[i+j] != t[j]:
            c += 1
    minc = min(minc, c)

print(minc)

