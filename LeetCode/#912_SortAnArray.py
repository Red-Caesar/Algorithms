nums = [5,1,1,2,0,0]

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        support = arr[len(arr)//2]
        new_arr = arr[:len(arr)//2] + arr[len(arr)//2 + 1:]
        low = [i for i in new_arr if i <= support]
        high = [i for i in new_arr if i > support]
        return quick_sort(low) + [support] + quick_sort(high)
print(quick_sort(nums))