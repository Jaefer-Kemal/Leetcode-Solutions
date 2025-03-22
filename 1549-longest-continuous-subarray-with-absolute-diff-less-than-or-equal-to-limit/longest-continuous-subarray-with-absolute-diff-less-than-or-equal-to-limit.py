class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()
        min_deque = deque()

        left = 0
        ans = 0
        for right in range(len(nums)):

            while max_deque and nums[max_deque[-1]] < nums[right]:
                max_deque.pop()
            
            while min_deque and nums[min_deque[-1]] > nums[right]:
                min_deque.pop()
            
            max_deque.append(right)
            min_deque.append(right)

            while (max_deque and min_deque) and (nums[max_deque[0]] - nums[min_deque[0]]) > limit:
                if left == max_deque[0]:
                    max_deque.popleft()
                
                if left == min_deque[0]:
                    min_deque.popleft()
                
                left += 1

            
            ans = max(ans, right - left + 1)

        return ans