def B():
    a = [list(map(int, input().split())) for i in range(3)]
    n = int(input())
    b = [int(input()) for i in range(n)]

    for i in range(3):
        for j in range(3):
            for k in range(n):
                if(a[i][j] == b[k]):
                    a[i][j] = 1  

    if all(a[i][i] == 1 for i in range(3)) or (a[0][2] == a[1][1] == a[2][0] == 1):
        print("Yes")
        return
    else:
        for i in range(3):
            if all(a[i][j] == 1 for j in range(3)) or all(a[j][i] == 1 for j in range(3)):
                print("Yes")
                return

    print("No")

B()