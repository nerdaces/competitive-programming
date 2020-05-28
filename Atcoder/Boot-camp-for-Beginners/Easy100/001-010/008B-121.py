def B():
    a, b = map(str, input().split())

    s = ''.join([a, b])
    s = int(s)

    for i in range(1, 1010):
        if(s % i == 0 and s / i == i):
            print('Yes')
            return
    
    print('No')

B()
