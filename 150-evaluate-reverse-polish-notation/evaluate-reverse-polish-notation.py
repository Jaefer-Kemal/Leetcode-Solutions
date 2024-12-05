class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        operator = {"+","-","/","*"}
        for r in range(len(tokens)):
            if tokens[r] in operator:
    
                a = int(stack.pop())
                b = int(stack.pop())
                if tokens[r] == "+":
                    res = a + b
                elif tokens[r] == "-":
                    res = b - a
                elif tokens[r] == "/":
                    res = b / a
                elif tokens[r] == "*":
                    res = a * b
                stack.append(res)
            else:
                stack.append(tokens[r])
  

        return int(stack[-1])
