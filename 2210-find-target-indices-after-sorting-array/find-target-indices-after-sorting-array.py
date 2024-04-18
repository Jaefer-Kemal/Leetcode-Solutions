class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res=[]
        for index,num in enumerate(nums):
            if num==target:
                res.append(index)
        return res
        