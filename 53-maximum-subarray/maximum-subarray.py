class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = 0
        maximum_sum = float("-inf")
        left = 0

        for right in range(len(nums)):
            if nums[right] > maximum_sum:
                maximum_sum = nums[right]
            
            prefix_sum += nums[right]
            
            if prefix_sum < 0:
                left = right + 1
                prefix_sum = 0
                continue
            
            if prefix_sum > maximum_sum:
                maximum_sum = prefix_sum

        return maximum_sum
            
        