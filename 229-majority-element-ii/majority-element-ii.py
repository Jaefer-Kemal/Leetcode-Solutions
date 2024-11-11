from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        
        n = len(nums)
        n = n//3
        res = []
        for key, value in c.items():
            if value > n:
                res.append(key)
                
        return res
                
        