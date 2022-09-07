class Solution:
    def reverseBits(self, n: int) -> int:
        int(bin(n)[2:].rjust(32, '0')[::-1], 2)


s = Solution()
print(s.reverseBits(0b00000010100101000001111010011100))
print(s.reverseBits(0b11111111111111111111111111111101))
