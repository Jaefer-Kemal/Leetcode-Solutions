class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        read=0
        write=0
        while read<len(nums):
            if nums[read]!=0:
                nums[read],nums[write]=nums[write],nums[read]
                write+=1
            read+=1
        """
        Do not return anything, modify nums in-place instead.
        """
        