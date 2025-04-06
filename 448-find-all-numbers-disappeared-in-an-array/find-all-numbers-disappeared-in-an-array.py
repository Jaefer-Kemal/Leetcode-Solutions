class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for index, num in enumerate(nums):
            correct_position = abs(num) - 1
            if nums[correct_position] > 0:
                nums[correct_position] *= -1
            
        res = []
        for index in range(len(nums)):
            if nums[index] > 0:
                res.append(index + 1)
        
        return res
