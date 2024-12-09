class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = defaultdict(int)

        for r in range(k + 1):
            if len(nums) == r:
                return False
            seen[nums[r]] += 1
            if seen[nums[r]] > 1:
                return True
            
        l = 0
        for r in range(k + 1,len(nums)):
            seen[nums[l]] -= 1
            if seen[nums[l]] == 0:
                del seen[nums[l]]
            seen[nums[r]] += 1
            if seen[nums[r]] > 1:
                return True
            l += 1
        return False


            
                
        