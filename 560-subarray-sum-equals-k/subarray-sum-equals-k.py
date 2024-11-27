class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ct = defaultdict(int)
        ct[0] = 1
        ans = 0
        sum_ = 0
        for r in range(len(nums)):
            sum_ += nums[r]
            ans += ct[sum_-k]
            ct[sum_] += 1
        
        return ans