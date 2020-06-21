def f(n):
    a = []
    while n > 0:
        n -= 1
        a.append(chr(ord('a') + n % 26))
        n //= 26
    return a

if __name__ == "__main__":
    n = int(input())
    a = f(n)
    print(''.join(a[::-1]))
