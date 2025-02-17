class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = [nums[0]]
        sum_ = nums[0]
        for i in range(1, len(nums)):
            sum_ += nums[i]
            running_sum.append(sum_)
        
        return running_sum