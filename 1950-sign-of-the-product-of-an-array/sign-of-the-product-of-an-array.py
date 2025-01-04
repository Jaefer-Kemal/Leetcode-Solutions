class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg_val = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                neg_val += 1
        
        return 1 if neg_val % 2 == 0 else -1