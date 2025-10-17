class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums_count = Counter(nums)
        res = 0

        for num, val in nums_count.items():
            if val == 1:
                res += num
        
        return res
            

        