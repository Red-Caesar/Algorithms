from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        hash_table = dict()
        for word in words:
            if word not in hash_table:
                hash_table[word] = 1
            else:
                hash_table[word] += 1
        cnt = 0
        isAlone = False
        for word in hash_table.keys():
            if word[::-1] in hash_table and word[0] != word[1]:
                cnt += min(hash_table[word], hash_table[word[::-1]])
            elif word[0] == word[1]:
                cnt += (hash_table[word] // 2) * 2
                if not isAlone:
                    isAlone = (hash_table[word] % 2 == 1)
        return cnt*2 + 2*int(isAlone)


s = Solution()
# print(s.longestPalindrome(["lc","cl","gg"]))
# print(s.longestPalindrome(["ab","ty","yt","lc","cl","ab"]))
# print(s.longestPalindrome(["cc","ll","xx"]))
print(s.longestPalindrome(["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]))
