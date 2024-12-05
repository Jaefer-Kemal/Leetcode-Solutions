class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = float("inf")
        

    def push(self, val: int) -> None:
        if self.minimum > val:
            self.minimum = val
        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if self.stack:
            if self.minimum == popped:
                self.minimum = min(self.stack)
        else:
            self.minimum = float("inf")

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if self.minimum == float("inf"):
            return None
        return self.minimum
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()