class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        pass
    def first_solution(self, s: str, k: int) -> int:
        hash_table = dict()
        maximum = 0
        start = 0
        for i in range(len(s)):
            if s[i] not in hash_table:
                hash_table[s[i]] = 1
            else:
                hash_table[s[i]] += 1
            local_max = max(hash_table.values())
            if maximum < local_max:
                maximum = local_max
            cnt = - local_max
            for key, val in hash_table.items():
                cnt += val
            if cnt > k:
                for j in range(start, i):
                    hash_table[s[j]] -= 1
                    new_local_max = max(hash_table.values())
                    new_cnt = - new_local_max
                    for key, val in hash_table.items():
                        new_cnt += val
                    if new_cnt <= k:
                        start = j+1
                        break

        return (maximum + k if maximum + k <= len(s) else len(s))

    def second_solution(self, s: str, k: int) -> int:
        hash_table = dict()
        maximum = 0
        i = 0
        start = 0
        while i < len(s):
            if s[i] not in hash_table:
                hash_table[s[i]] = 1
            else:
                hash_table[s[i]] += 1
            len_win = i - start + 1
            local_max = max(hash_table.values())
            cnt = len_win - local_max
            if cnt > k:
                if hash_table[s[start]] == 1:
                    del hash_table[s[start]]
                else:
                    hash_table[s[start]] -= 1
                start += 1
            else:
                maximum = max(maximum, len_win)
            i += 1
        return maximum


s = Solution
print(s.second_solution(s, "AAAA", 2))
print(s.second_solution(s, "ACBMCCA", 1))
print(s.second_solution(s, "ABAB", 2))
print(s.second_solution(s, "AABABBA", 1))
