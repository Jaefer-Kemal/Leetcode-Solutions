from queue import Queue

class MyStack:
    def __init__(self):
        self.in_queue = deque()
        self.out_queue = deque()

    def push(self, x: int) -> None:
        self.in_queue.append(x)
        self.top_stack = x

    def pop(self) -> int:
        self.pop_operation()
        return self.popped

    def top(self) -> int:
        return self.top_stack

    def empty(self) -> bool:
        return len(self.in_queue) == 0

    def pop_operation(self):
        self.out_queue = deque()

        while self.in_queue:
            self.bottom_stack = self.in_queue.popleft()

            if len(self.in_queue) != 0:
                self.out_queue.append(self.bottom_stack)
                self.top_stack = self.bottom_stack
            else:
                self.popped = self.bottom_stack 
        
        self.in_queue = self.out_queue

        
    

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()