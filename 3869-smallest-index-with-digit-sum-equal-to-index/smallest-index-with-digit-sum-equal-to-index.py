class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        for index, num in enumerate(nums):
            digit_sum = 0
            while num:
                digit_sum += num % 10
                num //= 10
            
            if digit_sum == index:
                return index
        
        return -1

        