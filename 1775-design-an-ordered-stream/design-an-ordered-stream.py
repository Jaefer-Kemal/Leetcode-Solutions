class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * (n + 1)
        self.ptr = 1
        

    def insert(self, idKey: int, value: str) -> List[str]:
        res = []
        self.stream[idKey] = value
        
        for i in range(self.ptr, len(self.stream)):
            if self.stream[i] != None:
                res.append(self.stream[i])
                self.ptr += 1
            else:
                break
        
        return res
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)