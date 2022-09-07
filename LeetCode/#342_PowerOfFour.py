from math import log
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        cnt = 0
        while n > 4**cnt:
            cnt += 1
        return n == 4**cnt

    def SecondSolution(self, n: int) -> bool:
        # return (n == 1 or n%4 == 0) and all([n%x != 0 for x in [3,5,6,7,9]])
        return n > 0 and log(n, 4).is_integer()
s = Solution
print(s.SecondSolution(s, 16))
print(s.SecondSolution(s, 5))
print(s.SecondSolution(s, 1))
print(s.SecondSolution(s, 33))
