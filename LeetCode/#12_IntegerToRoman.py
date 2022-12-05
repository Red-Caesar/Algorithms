class Solution:
    def intToRoman(self, num: int) -> str:
        hash_map = {1 : 'I', 5 : 'V', 10 : 'X', 50 : 'L', 100 : 'C', 500 : 'D', 1000 : 'M' }
        cnt = 0
        s = ""
        while num > 0:
            n = num % 10
            num //= 10
            if n < 4:
                s = hash_map[1*(10**cnt)] * n + s
            elif n == 4:
                s = hash_map[1*(10**cnt)] + hash_map[5*(10**cnt)] + s
            elif n < 9:
                s = hash_map[5*(10**cnt)] + hash_map[1*(10**cnt)]*(n - 5) + s
            elif n == 9:
                s = hash_map[1*(10**cnt)] + hash_map[1*(10**(cnt+1))] + s
            cnt += 1
        
        return s

s = Solution()
print(s.intToRoman(3))
print(s.intToRoman(58))
print(s.intToRoman(1994))
