class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []


    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if not self.out_stack:
            self.out_stack = self.in_stack.copy()[::-1]
            self.in_stack = []

        return self.out_stack.pop()
        

    def peek(self) -> int:
        if not self.out_stack:
            self.out_stack = self.in_stack.copy()[::-1]
            self.in_stack = []
        
        return self.out_stack[-1]

    def empty(self) -> bool:
        if not self.out_stack:
            self.out_stack = self.in_stack.copy()[::-1]
            self.in_stack = []

        return len(self.out_stack) == 0
        

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()