n = int(input())
a = list(map(int, input().split()))
node = a[n]
cnt = a[n]

while n - 1 > 1:
    node += a[n-1] - a[n]
    cnt += node
    n -= 1

print(cnt+1)