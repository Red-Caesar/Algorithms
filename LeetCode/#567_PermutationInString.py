class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_s1 = dict()
        for c in s1:
            if c not in hash_s1:
                hash_s1[c] = 1
            else:
                hash_s1[c] += 1
        window_start, window_end = 0, 0
        while window_end < len(s2):
            if not hash_s1:
                return True
            if s2[window_end] in hash_s1:
                if hash_s1[s2[window_end]] == 1:
                    del hash_s1[s2[window_end]]
                else:
                    hash_s1[s2[window_end]] -= 1
                window_end += 1
            else:
                if s2[window_start] not in hash_s1:
                    hash_s1[s2[window_start]] = 1
                else:
                    hash_s1[s2[window_start]] += 1
                window_start += 1
        return not bool(hash_s1)


s = Solution()
print(s.checkInclusion("ab", "eidbaooo"))
print(s.checkInclusion("ab", "eidboaoo"))
print(s.checkInclusion("adc", "dcda"))
