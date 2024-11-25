class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        count = 0
        maximum = float("-inf")

        for r in range(len(nums)):
            cur_sum += nums[r]
            maximum = max(maximum,cur_sum)
            if cur_sum < 0:
                cur_sum = 0
               
        return maximum
        