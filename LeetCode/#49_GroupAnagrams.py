from typing import List
import string 


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters = string.ascii_lowercase
        cnt = 1
        pow = 0
        table = dict()
        for c in letters:
            table[c] = cnt*(10**pow)
            cnt += 1
            pow += 1
        hash_map = dict()
        for s in strs:
            amount = 0
            for c in s:
                amount += table[c]
            if amount not in hash_map:
                hash_map[amount] = [s]
            else:
                hash_map[amount].append(s)
        return list(hash_map.values())


s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["a"]))
