k, n = map(int, input().split())
a = list(map(int, input().split()))
sum_s, sum_o = 0, 0

for i in range(n-1):
    sum_o += a[i+1] - a[i]

a_ex1 = [i for i in a if i <= k // 2]
a_ex2 = [i for i in a if i > k // 2]
if len(a_ex1) != 0 and len(a_ex2) != 0:
    sum_s = max(a_ex1) + k - min(a_ex2)
elif len(a_ex1) == 0:
    sum_s = max(a_ex2) - min(a_ex2)
else:
    sum_s = max(a_ex1) - min(a_ex1)

# print(a_ex1)
# print(a_ex2)

print(min(sum_o, sum_s))
