class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            correct_position = abs(num) - 1
            
            if nums[correct_position] < 0:
                res.append(abs(num))
            
            else:
                nums[correct_position] *= -1

        
        for index in range(len(nums)):
            
            if nums[index] > 0:
                res.append(index + 1)
        
        return res