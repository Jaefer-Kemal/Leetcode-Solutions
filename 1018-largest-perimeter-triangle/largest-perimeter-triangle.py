class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
    
        for r in range(len(nums) - 2):
            if nums[r] < nums[r + 1] + nums[r + 2]:
                return nums[r] + nums[r + 1] + nums[r + 2]
            
        return 0