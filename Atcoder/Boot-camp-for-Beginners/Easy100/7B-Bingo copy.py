a = [list(map(int, input().split())) for i in range(3)]
n = int(input())
b = [int(input()) for i in range(n)]

for i in range(3):
    for j in range(3):
        for k in range(n):
            if(a[i][j] == b[k]):
                a[i][j] = 1
            else:
                a[i][j] = 0

if((a[0][0] == a[1][1] == a[2][2] == 1) or (a[0][2] == a[1][1] == a[2][0] == 1)):
    print("Yes")
else:
    for i in range(3):
        c = 0
        if(a[i] == [1,1,1]):
            print("Yes")
            break
        else:
            for j in range(3):
                if(a[j][i] == 1):
                    c += 1
                else:
                    break
            if(c == 3):
                print("Yes")
                break