a,b,c= map(int,input().split())

# a%=10
# if b>4:
#     b=b%4+4
# if c>4:
#     c=c%4+4
# x=pow(a,pow(b,c))
# print(x%10)

print(pow(a%10,pow(b,c,4)))