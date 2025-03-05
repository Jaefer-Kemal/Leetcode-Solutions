class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.value = value
        self.k = k
        self.unwanted = defaultdict(int)

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        flag = False
        if num != self.value:
            self.unwanted[num] += 1

        if len(self.queue) < self.k:
            return False
        
        if self.queue[0] != self.value:
            flag = True
            self.unwanted[self.queue[0]] -= 1
            if self.unwanted[self.queue[0]] == 0:
                del self.unwanted[self.queue[0]] 

        self.queue.popleft()

        if self.unwanted or flag:
            return False
        
        return True
        
    



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)