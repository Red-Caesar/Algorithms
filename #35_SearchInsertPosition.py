nums = [1,3,5,6]
target = 7
def bin_search(arr, index):
    if len(arr) == 1:
        return index if nums[index] >= target else index+1
    k = len(arr)//2
    if target == arr[k]:
        return index
    elif target > arr[k]:
        ans = bin_search(arr[k:], index + (len(arr[k:])//2))
    elif target < arr[k]:
        diff = (len(arr[:k])//2)
        ans = bin_search(arr[:k], index - (len(arr[:k]) - diff))
    return ans

ans = bin_search(nums, len(nums)//2)
print(ans)
