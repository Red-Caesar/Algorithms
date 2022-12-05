# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    picked = 6
    if num < picked:
        return 1
    elif num > picked:
        return -1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        start = -1
        end = n+1
        while guess((start+end)//2) != 0:
            if guess((start+end)//2) == -1:
                end = (start+end)//2
            else:
                start = (start+end)//2
                
        return (start+end)//2
            
s = Solution()
print(s.guessNumber(10))