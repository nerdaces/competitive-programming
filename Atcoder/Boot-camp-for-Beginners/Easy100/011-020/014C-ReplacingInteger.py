n, k = map(int, input().split())

# print(abs(n - k * round(n / k)))
a = n % k
print(min(a, abs(a - k)))