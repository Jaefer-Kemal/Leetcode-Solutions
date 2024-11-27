from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        c = {"{":"}", "[":"]", "(":")"}
        for i in range(len(s)):
            if s[i] in c.keys():
                stack.append(s[i])
            else:
                if not stack:
                    return False
                a = stack.pop()
                if c[a] != s[i]:
                    return False
        if stack:
            return False
        return True


        