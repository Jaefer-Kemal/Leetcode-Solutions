from collections import deque
from typing import List

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left = 0
        count = 0
        min_deque = deque()
        max_deque = deque()
        
        for right in range(len(nums)):
            # Update min_deque
            while min_deque and nums[right] <= nums[min_deque[-1]]:
                min_deque.pop()
            min_deque.append(right)
            
            # Update max_deque
            while max_deque and nums[right] >= nums[max_deque[-1]]:
                max_deque.pop()
            max_deque.append(right)
            
            # Shrink window if invalid
            while max_deque and min_deque and nums[max_deque[0]] - nums[min_deque[0]] > 2:
                if min_deque[0] == left:
                    min_deque.popleft()
                if max_deque[0] == left:
                    max_deque.popleft()
                left += 1

            # Count valid subarrays ending at `right`
            count += right - left + 1
        
        return count
