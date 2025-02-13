class Solution: 
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_difference = float("inf")
        closest_sum = float("inf")

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[left] + nums[right] + nums[i]

                if min_difference > abs(target - current_sum):
                    min_difference = abs(target - current_sum)
                    closest_sum = current_sum
                    
                if current_sum == target:
                    return current_sum

                elif current_sum > target:
                    right -= 1
                    
                else:
                    left += 1
        
        return closest_sum