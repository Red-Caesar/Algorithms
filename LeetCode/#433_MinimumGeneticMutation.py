from typing import List
from collections import deque


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if not bank:
            return -1

        isVisited = [False for _ in range(len(bank))]
        path = deque()
        path.append(start)
        cnt = 0
        while path:
            for _ in range(len(path)):
                gen = path.popleft()
                for j in range(len(bank)):
                    diff = 0
                    for i in range(len(gen)):
                        if gen[i] != bank[j][i]:
                            diff += 1
                    if diff == 1 and not isVisited[j]:
                        isVisited[j] = True
                        path.append(bank[j])
                    elif diff == 0 and gen == end:
                        return cnt
            cnt += 1
        return -1


s = Solution()
print(s.minMutation(start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]))
print(s.minMutation(start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]))
print(s.minMutation(start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]))
