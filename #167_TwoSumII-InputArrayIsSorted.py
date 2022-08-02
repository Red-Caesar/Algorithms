numbers = [-1, 0]
target = -1


# def bin_search(arr, index):
#     if len(arr) == 1:
#         return index if numbers[index] >= target else index + 1
#     k = len(arr) // 2
#     if target == arr[k]:
#         return index
#     elif target > arr[k]:
#         ans = bin_search(arr[k:], index + (len(arr[k:]) // 2))
#     elif target < arr[k]:
#         diff = (len(arr[:k]) // 2)
#         ans = bin_search(arr[:k], index - (len(arr[:k]) - diff))
#     return ans
#
#
# index = bin_search(numbers, len(numbers) // 2)
# reverse = False
# if index == len(numbers) or numbers[index] >= 0:
#     numbers = numbers[:index]
# else:
#     numbers = numbers[index:]
#     reverse = True
#
# if len(numbers) == 2:
#     return ([1, 2]) if not reverse else ([index, index + 1])
# else:
#     start = 0
#     end = len(numbers) - 1
#     while start <= end:
#         sum = numbers[start] + numbers[end]
#         if sum == target:
#             return (start + 1, end + 1)
#             break
#         elif sum < target:
#             end -= 1
#         else:
#             start += 1
start = 0
end = len(numbers) - 1
while start <= end:
    sum = numbers[start] + numbers[end]
    if sum == target:
        print ([start + 1, end + 1])
        break
    elif sum < target:
        start += 1
    else:
        end -= 1