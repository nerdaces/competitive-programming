def calc(nodes,y,cost,costs):
    for i in a:
        if i==y:
            return costs
        else:
            cost+=1
            costs.append(calc(nodes[i],y,cost,costs))
    return costs

n,m,x,y=map(int, input().split())
a,b,t,k=[0] * m, [0] * m, [0] * m, [0] * m
nodes,costs,spaces=[[]],[[]],[[]]
for i in range(m):
    a[i], b[i], t[i], k[i] = map(int, input().split())
    nodes[a[i]].append[b[i]]
    costs[a[i]].append[t[i]]
    spaces[a[i]].append[k[i]]
    nodes[b[i]].append[a[i]]
    costs[b[i]].append[t[i]]
    spaces[b[i]].append[k[i]]

clock=0

