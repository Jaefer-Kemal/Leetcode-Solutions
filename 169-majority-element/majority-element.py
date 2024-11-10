from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        
        maxim = -1
        res = nums[0]
        for key, value in c.items():
            if value > maxim:
                maxim = value
                res = key
        
        return res
        
        