class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for char in s:
            if char == ")":
                last = stack.pop()
                stack[-1] += max(last * 2, 1)
            
            else:
                stack.append(0)
        
        return stack[-1]