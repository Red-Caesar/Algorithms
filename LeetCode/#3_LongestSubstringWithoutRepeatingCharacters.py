class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        end = 0
        maximum = 0
        slide = ''
        while end < len(s):
            if s[end] not in slide:
                slide += s[end]
                end += 1
            else:
                slide = slide[1:]
            maximum = max(maximum, len(slide))
        return maximum


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("aa"))