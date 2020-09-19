s = input()
t = input()

for i in range(len(t)):
    if t[:len(t)-i] in s:
        print(i)
        exit()

print(0)

