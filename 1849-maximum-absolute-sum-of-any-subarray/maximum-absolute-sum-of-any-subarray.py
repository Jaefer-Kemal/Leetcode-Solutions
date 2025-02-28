class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        positive_sum = 0
        negative_sum = 0

        maximum_sum = 0
        minimum_sum = 0
        for i in range(len(nums)):
            positive_sum += nums[i]
            negative_sum += nums[i]

            if positive_sum < 0:
                positive_sum = 0

            if negative_sum > 0:
                negative_sum = 0

            maximum_sum = max(maximum_sum, positive_sum)
            minimum_sum = min(minimum_sum, negative_sum)

        return max(abs(minimum_sum), maximum_sum)