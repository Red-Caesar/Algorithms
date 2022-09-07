from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
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
        return(ans)

    def SecondSolution(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high -= 1
            else:
                low += 1
        return low if nums[low] >= target else low+1

s = Solution
print(s.SecondSolution(s,  nums = [1,3,5,6], target = 5))
print(s.SecondSolution(s, nums = [1,3,5,6], target = 2))
print(s.SecondSolution(s, nums = [1,3,5,6], target = 7))
print(s.SecondSolution(s, nums = [2,5], target = 6))