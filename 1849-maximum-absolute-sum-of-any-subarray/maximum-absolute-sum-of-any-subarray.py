class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix_sum = 0
        maximum_sum_1 = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum < 0:
                prefix_sum = 0
            maximum_sum_1 = max(maximum_sum_1, prefix_sum)

        prefix_sum = 0
        maximum_sum_2 = 0
        for i in range(len(nums)):
            prefix_sum += (-nums[i])
            if prefix_sum < 0:
                prefix_sum = 0
            maximum_sum_2 = max(maximum_sum_2, prefix_sum)

        return max(maximum_sum_1, maximum_sum_2)