class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = 0
        
        for right in range(k):
            current_sum += nums[right]

        maximum_average = current_sum / k
        
        left = 0
        for right in range(k, len(nums)):
            current_sum -= nums[left]
            current_sum += nums[right]
            left += 1
            
            current_average = current_sum / k
            maximum_average = max(maximum_average, current_average)

        return maximum_average