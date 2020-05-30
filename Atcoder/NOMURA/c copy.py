n = int(input())
a = list(map(int, input().split()))
node = 0
cnt = 0

if a[0] == 0:
    node += 1
    cnt += 1
    for i in range(1, len(a)):
        if n > i:
            if node * 2 > a[i]:
                node = (node - a[i-1]) * 2
                cnt += node
            else:
                print(-1)
                break
        else:
            print(cnt + a[i])
            break
else:
    print(-1)