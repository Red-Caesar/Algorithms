from typing import List
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if not tokens:
            return 0
        score = 0
        tokens.sort()
        start = 0
        end = len(tokens) - 1
        mx = 0
        while start <= end:
            if tokens[start] <= power:
                score += 1
                mx = max(mx, score)
                power -= tokens[start]
                start += 1
            elif score > 0:
                score -= 1
                power += tokens[end]
                end -= 1
            else:
                break
        return mx



s = Solution()
print(s.bagOfTokensScore([100], 50))
print(s.bagOfTokensScore([100,200], 150))
print(s.bagOfTokensScore([100,200,300,400], 200))
print(s.bagOfTokensScore([], 10))
print(s.bagOfTokensScore([91,4,75,70,66,71,91,64,37,54], 20))