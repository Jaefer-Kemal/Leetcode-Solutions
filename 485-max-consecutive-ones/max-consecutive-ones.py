class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum_ones = 0
        l = 0
        count = 0
        while l < len(nums):
            if nums[l] != 0:
                count += 1
            else:
                maximum_ones = max(count, maximum_ones)
                count = 0
            
            l += 1
        
        return max(maximum_ones, count)