# import math

N = int(input())

# of = math.floor(N / 108 * 100)
# oc = math.ceil(N / 108 * 100)
o = round(N / 108 * 100)

# if(int(of * 108 / 100) != N and int(oc * 108 / 100) != N):
if round(o * 108 / 100) != N:
    print(":(")
else:
    print(o)