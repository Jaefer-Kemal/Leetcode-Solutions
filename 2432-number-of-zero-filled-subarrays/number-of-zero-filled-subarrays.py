class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        occurence = 0
        for num in nums:
            if num == 0:
                count += 1
                occurence += count
            
            else:
                count = 0
            
        return occurence
          