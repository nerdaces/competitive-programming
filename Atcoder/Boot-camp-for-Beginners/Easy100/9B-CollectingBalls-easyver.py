n = int(input())
k = int(input())
x = list(map(int, input().split()))
sum = 0

for i in range(n):
    sum += min(x[i], k-x[i]) * 2

print(sum)