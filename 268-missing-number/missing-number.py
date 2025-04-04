class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count_arr = [0] * (len(nums) + 1)

        for num in nums:
            count_arr[num] = 1

        for index, mark in enumerate(count_arr):
            if mark == 0:
                return index