class Solution:

    def __init__(self, nums: List[int]):
        self.nums_index = defaultdict(list)
        for index, num in enumerate(nums):
            self.nums_index[num].append(index)
        

    def pick(self, target: int) -> int:
        return random.choice(self.nums_index[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)