class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count_size = max(nums) + 1
        count_arr = [0] * count_size
        prefix_sum = [0] * count_size

        for num in nums:
            count_arr[num] += 1

        prefix_sum[0] = count_arr[0]

        for i in range(1, count_size):
            prefix_sum[i] = count_arr[i] + prefix_sum[i - 1]

        results = []

        for num in nums:
            results.append(prefix_sum[num] - count_arr[num])

        return results      