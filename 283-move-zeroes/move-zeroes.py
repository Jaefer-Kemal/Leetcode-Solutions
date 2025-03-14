class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        holder = 0
        seeker = 1

        while seeker < len(nums) and holder < len(nums):
            if nums[seeker] != 0:
                if nums[holder] == 0:
                    nums[seeker], nums[holder] = nums[holder], nums[seeker]
                    
                    holder += 1
                    seeker += 1
                else:
                    holder += 1
                    if holder >= seeker:
                        seeker += 1
            else:
                seeker += 1

