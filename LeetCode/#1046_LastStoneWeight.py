from typing import List
from heapq import heapify, heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def binary_search(start, end, val, arr):
            while start < end:
                mid = (start + end) // 2
                if val < arr[mid]:
                    start += 1
                elif val > arr[mid]:
                    end -= 1
                else:
                    return mid
            return start+1 if start < len(arr) and val < arr[start] else start

        stones = sorted(stones, reverse=True)
        while len(stones) > 1:
            round = abs(stones[0] - stones[1])
            stones.pop(0)
            stones.pop(0)
            if round != 0:
                id = binary_search(0, len(stones)-1, round, stones)
                stones.insert(id, round)

        return 0 if not stones else stones[0]

    def SecondSolution(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        while len(stones) > 1:
            heapify(stones)
            two_stones = [-heappop(stones), -heappop(stones)]
            round = abs(two_stones[0] - two_stones[1])
            if round != 0:
                heappush(stones, -round)

        return 0 if not stones else -stones[0]


s = Solution
print(s.SecondSolution(s, [2,7,4,1,8,1]))
print(s.SecondSolution(s, [1]))
print(s.SecondSolution(s, [7,6,7,6,9]))
print(s.SecondSolution(s, [316,157,73,106,771,828,46,212,926,604,600,992,71,51,477,869,425,405,859,924,45,187,283,590,303,66,508,982,464,398]))

