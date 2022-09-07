from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        def helper(num):
            if len(num) == n:
                if num[0] != 0:
                    ans.append(int(''.join(map(str, num))))
                return
            else:
                for i in range(10):
                    if not num:
                        helper([i])
                    else:
                        if abs(num[-1] - i) == k:
                            helper(num + [i])

        helper([])
        return ans

s = Solution()
print(s.numsSameConsecDiff(3, 7))
print(s.numsSameConsecDiff(2, 1))
print(s.numsSameConsecDiff(2, 0))
