class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        res = 0
        for token in tokens:
            if token in "+-*/":

                num1 = int(stack.pop())
                num2 = int(stack.pop())

                match token:
                    case "+":
                        res = num2 + num1
                    case "-":
                        res = num2 - num1
                    case "*":
                        res = num2 * num1
                    case "/":
                        res = num2 / num1
                        if res < 0:
                            res = ceil(res)
                        else:
                            res = floor(res)

                stack.append(res)

            else:
                stack.append(token)
                
        return int(stack[-1])