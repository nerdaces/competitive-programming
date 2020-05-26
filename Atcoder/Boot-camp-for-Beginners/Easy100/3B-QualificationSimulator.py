N, A, B = list(map(int, input().split()))
S = input()
y, yab = 0, 1

for s in S:
    if(s == 'a'):
        if(y < A + B):
            print("Yes")
            y += 1
        else:
            print("No")
    elif(s == 'b'):
        if(y < A + B and yab <= B):
            print("Yes")
            y += 1
            yab += 1
        else:
            print("No")
    else:
        print("No")