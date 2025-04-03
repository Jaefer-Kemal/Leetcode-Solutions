class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        res = []
        
        while i < n:
            correct_position = abs(nums[i]) - 1

            if nums[correct_position] < 0:
                res.append(abs(nums[i]))
            
            else:
                nums[correct_position] *= -1

            i += 1

        return res