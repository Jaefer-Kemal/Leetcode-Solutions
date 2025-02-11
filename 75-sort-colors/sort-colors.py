class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes_count = 0
        ones_count = 0
        twos_count = 0
        size = len(nums)
        for i in range(size):
            if nums[i] == 0:
                zeroes_count += 1
            elif nums[i] == 1:
                ones_count += 1
            else:
                twos_count += 1
        
        for i in range(size):
            if zeroes_count:
                nums[i] = 0
                zeroes_count -= 1
            elif ones_count:
                nums[i] = 1
                ones_count -= 1
            else:
                nums[i] = 2
        