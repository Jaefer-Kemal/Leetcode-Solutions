class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0]
        accumulator = 0
        for i in range(len(nums)):
            accumulator += nums[i]
            self.prefix_sum.append(accumulator)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)