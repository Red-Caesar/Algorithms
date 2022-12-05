class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if stack[-1].lower() == c.lower() and stack[-1] != c:
                    stack.pop()
                else:
                    stack.append(c)
        return "".join(stack)

        


s = Solution()
print(s.makeGood("leEeetcode"))
print(s.makeGood("abBAcC"))
print(s.makeGood("s"))
