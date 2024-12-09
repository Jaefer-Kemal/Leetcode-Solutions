from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = defaultdict(int)
        l = 0
        
        for r in range(len(nums)):
            if nums[r] in seen and seen[nums[r]] >= 1:
                return True
            
            seen[nums[r]] += 1
            
            if r - l >= k:
                seen[nums[l]] -= 1
                l += 1
        
        return False
