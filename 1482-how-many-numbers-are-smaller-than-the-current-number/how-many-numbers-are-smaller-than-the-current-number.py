class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        maximum_element = max(nums) + 1
        count_arr = [0] * maximum_element
        prefix_count_arr = [0] * maximum_element

        for num in nums:
            count_arr[num] += 1
        prefix_count_arr[0] = count_arr[0]
        for i in range(1, maximum_element):
            prefix_count_arr[i] = count_arr[i] + prefix_count_arr[i - 1]

        results = []

        for num in nums:

            results.append(prefix_count_arr[num] - count_arr[num])

        return results      