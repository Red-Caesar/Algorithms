cost = [1,100,1,1,1,100,1,1,100,1]
top = len(cost)
for i in range(len(cost)):
    if i-2 >= 0:
        cost[i] += min(cost[i-1], cost[i-2])
print(min(cost[top-1], cost[top-2]))