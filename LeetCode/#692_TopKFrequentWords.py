from typing import List
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hash_table = dict()
        for el in words:
            if el not in hash_table:
                hash_table[el] = 1
            else:
                hash_table[el] += 1
        words_list = sorted(hash_table, key=lambda x: (-hash_table[x], x))
        return words_list[:k]

s = Solution
print(s.topKFrequent(s, ["i","love","leetcode","i","love","coding"], 2))
print(s.topKFrequent(s, ["the","day","is","sunny","the","the","the","sunny","is","is"], 4))