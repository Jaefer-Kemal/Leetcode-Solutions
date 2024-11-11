from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        

        n = len(nums)
        n = n//2
        for key, value in c.items():
            if value > n:
                return key
        
        