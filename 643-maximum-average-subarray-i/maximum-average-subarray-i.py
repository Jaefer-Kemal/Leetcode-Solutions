class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        current_sum = 0
        for right in range(k):
            current_sum += nums[right]

        maximum_sum = current_sum
        
        left = 0
        for right in range(k, len(nums)):
            current_sum -= nums[left]
            current_sum += nums[right]
            left += 1

            maximum_sum = max(maximum_sum, current_sum)

        maximum_average = maximum_sum / k

        return maximum_average