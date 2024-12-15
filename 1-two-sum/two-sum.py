class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        n = len(nums)
        for r in range(n):
            if target - nums[r] in seen:
                return [r,seen[target - nums[r]]]
            if nums[r] not in seen:
                seen[nums[r]] = r