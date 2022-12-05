prices = [3,2,1,2,9,10,15]
#1st solution
# profit = 0
# for i in range(len(prices)):
#     for j in range(i+1, len(prices)):
#         profit = max(profit, prices[j]-prices[i])
# print(profit)

#2nd solution
profit = 0
low = 1e5
for i in range(len(prices)):
    profit = max(profit, prices[i]-low)
    low = min(low, prices[i])
print(profit)