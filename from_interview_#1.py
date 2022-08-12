# Для n = 4 - такой:
# 4 3 2 1
# 4 3 2
# 4 3 1
# 4 3
# 4 2 1
# 4 2
# 4 1
# 4


# 1st solution
# n = 4
# arr = [i for i in range(n, 0, -1)]
# arr_bool = [0 for _ in range(n)]
# k = 0
# while 2**(n-1) > k:
#     s = ""
#     for i in range(n):
#         if not arr_bool[i]:
#             s += f'{arr[i]} '
#     cnt = 0
#     for i in range(n-1, 0, -1):
#         if i == n-1:
#             if arr_bool[i] == 1:
#                 cnt = 1
#             arr_bool[i] = (arr_bool[i] + 1) % 2
#         else:
#             if (arr_bool[i] == 1 and cnt == 1):
#                 arr_bool[i] = (arr_bool[i] + cnt) % 2
#                 cnt = 1
#             else:
#                 arr_bool[i] = (arr_bool[i] + cnt) % 2
#                 cnt = 0
#
#     print(s)
#     k += 1

# 2nd solution
n = 5


def rec(k, i, s):
    if k == n:
        print(s)
        return
    rec(k+1, i-1, s+f" {i-1}")
    rec(k+1, i-1, s)
rec(1, n, f"{n}")
