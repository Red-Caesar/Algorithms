from typing import List
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_map = dict()
        for el in nums:
            if el not in hash_map:
                hash_map[el] = 1
            else:
                hash_map[el] += 1
        for key, val in hash_map.items():
            if val == 1:
                return key


    def secondSolution(self, nums: List[int]) -> int:
        return reduce(lambda cnt, x: cnt ^ x, nums)

s = Solution()
print(s.singleNumber([2,2,1]))
print(s.singleNumber([4,1,2,1,2]))
print(s.singleNumber([1]))
print(s.secondSolution([2,2,1]))
print(s.secondSolution([4,1,2,1,2]))
print(s.secondSolution([1]))
