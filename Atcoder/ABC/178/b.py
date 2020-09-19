a,b,c,d = map(int, input().split())

ans = a * c
# if max (a,b) < 10**3 or max (c,d) < 10**3:
#     for i in range(a,b+1):
#         for j in range(c, d+1):
#             ans = max(i*j, ans)
#     print(ans)
# else:
for i in [a,b]:
    for j in [c,d]:
        ans = max(i*j, ans)
print(ans)
