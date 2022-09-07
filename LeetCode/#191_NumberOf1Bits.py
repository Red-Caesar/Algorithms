from functools import reduce
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        binary = bin(n)
        for c in binary:
            if c == '1':
                cnt += 1
        return cnt


    def secondSolution(self, n: int) -> int:
        binary = bin(n)[2:]
        return reduce(lambda cnt, x: int(cnt) + int(x), binary)

s = Solution()
print(s.hammingWeight(0b00000000000000000000000000001011))
print(s.secondSolution(0b00000000000000000000000000001011))
