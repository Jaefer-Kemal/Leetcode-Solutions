class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        res = nums[0]

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= nums[0]:
                low = mid + 1
            
            else:
                res = nums[mid]
                high = mid - 1
        
        return res