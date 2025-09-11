class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for num in nums:
            if num > first and num > second:
                return True

            elif num < first:
                first = num
            
            elif num > first and num < second:
                second = num
        
        return False
            