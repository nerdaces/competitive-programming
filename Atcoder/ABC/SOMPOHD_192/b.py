s = input()

cnt = 1
for i in s:
    if cnt % 2 == 1:
        if not i.islower():
            print('No')
            exit()
        else:
            cnt += 1
    else:
        if not i.isupper():
            print('No')
            exit()
        else:
            cnt += 1
print('Yes')