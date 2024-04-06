class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                nums[i-1] *= 2
                nums[i]=0
    
        pos=[]
        zero=[]
        for num in nums:
            if num!=0:
                pos.append(num)
            else:
                zero.append(num)

        res = pos+zero
        return res
        