class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = 10**6
        l = 0
        sum_ = 0 
        for r in range(len(nums)):
            sum_ += nums[r]
        
            while sum_ >= target:
                min_len = min(min_len,r - l + 1)
                sum_ -= nums[l]
                l += 1
                

        return min_len if min_len != 10**6 else 0