class Solution:
    def isValid(self, s: str) -> bool:
        check = {
            ")" : "(",
            "}" : "{",
            "]" : "["}

        stack = []

        for char in s:
            if char in "]})":
                if stack:
                    if stack[-1] == check[char]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(char)
        
        if not stack:
            return True

        return False

        