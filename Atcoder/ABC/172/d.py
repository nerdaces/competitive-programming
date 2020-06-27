# import sympy

# def func(k):
#     i = 1
#     cnt = 0
#     if k == 1:
#         return 1
#     while i*i <= k:
#         if k % i == 0:
#             cnt += 1
#             if i != k // i:
#                 cnt += 1
#         i += 1
#     return cnt

def num_divisors_table(n):
    table = [0] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            table[j] += 1
    
    return table

n = int(input())
sum = 0
t = num_divisors_table(n)
for i in range(1, n + 1):
    # sum += i * sympy.divisor_count(i)
    sum += i * t[i]

print(sum)
