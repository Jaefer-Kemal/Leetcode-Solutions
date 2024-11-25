from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        for key, value in c.items():
            if value == 1:
                return key