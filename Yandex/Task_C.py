n, k = map(int, input().split())
arr = list(map(int, input().split()))
# 1st solution

# isSorted = True
# for i in range(n-1):
#     if arr[i] > arr[i+1]:
#         isSorted = False
#         break
# if not isSorted:
#     new_arr = sorted(arr)
# else:
#     new_arr = arr
# hash_table = dict()
# for i in range(n):
#     if arr[i] not in hash_table:
#         id = new_arr.index(arr[i])
#         summary = 0
#         left = 1
#         right = 1
#         for _ in range(k):
#             if id - left >= 0 and id + right < len(new_arr):
#                 if abs(new_arr[id] - new_arr[id-left]) > abs(new_arr[id] - new_arr[id+right]):
#                     summary += abs(new_arr[id] - new_arr[id+right])
#                     right += 1
#                 else:
#                     summary += abs(new_arr[id] - new_arr[id-left])
#                     left += 1
#             elif id - left < 0:
#                 summary += abs(new_arr[id] - new_arr[id + right])
#                 right += 1
#             else:
#                 summary += abs(new_arr[id] - new_arr[id-left])
#                 left += 1
#         print(summary, end=' ')
#         hash_table[arr[i]] = summary
#     else:
#         print(hash_table[arr[i]], end=' ')

# 2nd solution

# dp = [[0 for _ in range(n)] for _ in range(n)]
# for i in range(n):
#     num = []
#     for j in range(i, n):
#         if i != j:
#             dp[i][j] = abs(arr[i]-arr[j])
#             num.append(dp[i][j])
#     p = i
#     while p-1 >= 0:
#         num.append(dp[p-1][i])
#         p -= 1
#     summary = 0
#     num = sorted(num)
#     for t in range(k):
#         summary += num[t]
#     print(summary, end=' ')

# 3rd solution
