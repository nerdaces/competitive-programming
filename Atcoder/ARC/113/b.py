a,b,c=map(int,input().split())
if a==1:
    print(1)
    exit()
elif b==1:
    print(a)
    exit()

b=int(str(b)[-1])
cycle=[b]
v=b
flag=False
for i in range(c+4):
    v*=b
    v=int(str(v)[-1])
    if v in cycle:
        flag=True
        break
    else:
        cycle.append(v)

if not flag:
    b_c=cycle[-1]
else:
    b_c=cycle[c % len(cycle) - 1]

a=int(str(a)[-1])
cycle=[a]
v=a
flag=False
for i in range(b_c+4):
    v*=a
    v=int(str(v)[-1])
    if v in cycle:
        flag=True
        break
    else:
        cycle.append(v)

if not flag:
    print(cycle[-1])
else:
    print(cycle[b_c % len(cycle) - 1])
# print(int(str(a**(b**c))[-1]))