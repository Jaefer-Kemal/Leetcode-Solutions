class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        for i in range(1,len(nums)):
            if i == len(nums) - 1 and nums[i] == nums[i - 1]:
                return True
            if nums[i] > nums[i - 1]:
                flag = True
                break
            elif nums[i] < nums[i-1]:
                flag = False
                break
        
        for i in range(1,len(nums)):
            if flag:
                if nums[i] < nums[i - 1]:
                    return False
            else:
                if nums[i] > nums[i - 1]:
                    return False
        return True

        