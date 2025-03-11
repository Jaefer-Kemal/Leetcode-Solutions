class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.value = value
        self.k = k
        self.invalid = 0

    def consec(self, num: int) -> bool:
        if num != self.value:
            self.invalid += 1

        if len(self.queue) < self.k:
            self.queue.append(num)
            if len(self.queue) == self.k and self.invalid == 0:
                return True
            return False

        self.queue.append(num)
        popped = self.queue.popleft()

        if popped != self.value:
            self.invalid -= 1

        if self.invalid == 0:
            return True
        
        return False

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)