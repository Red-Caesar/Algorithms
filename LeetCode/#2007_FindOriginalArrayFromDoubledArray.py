from typing import List
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
        changed.sort()
        hash_map = dict()
        ans = []
        for el in changed:
            if el % 2 == 0 and el / 2 in hash_map:
                ans.append(el//2)
                if hash_map[el/2] == 1:
                    del hash_map[el/2]
                else:
                    hash_map[el/2] -= 1
            else:
                if el not in hash_map:
                    hash_map[el] = 1
                else:
                    hash_map[el] += 1
        
        if hash_map == {}:
            return ans
        else:
            return []   

s = Solution()
print(s.findOriginalArray([1,3,4,2,6,8]))
print(s.findOriginalArray([6,3,0,1]))
print(s.findOriginalArray([1]))
