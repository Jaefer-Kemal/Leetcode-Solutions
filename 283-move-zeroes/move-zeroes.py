class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        read = 0
        write = 0

        while read < len(nums):
            if nums[read] != 0:
                nums[read], nums[write] = nums[write], nums[read]
                
                write += 1
            read += 1

        '''First Solution'''
        # l = 0
        # r = 1
        # while r<len(nums):
        #     if nums[l] == 0 and nums[r] != 0:
        #         nums[l], nums[r] = nums[r], nums[l]
        #         l += 1
        #         r = l + 1
        #     elif nums[l] == 0 and nums[r] == 0:
        #         r += 1
        #     else:
        #         l += 1
        #         r = l + 1
            
            
