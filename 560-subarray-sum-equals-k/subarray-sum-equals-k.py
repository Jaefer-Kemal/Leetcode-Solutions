class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = {0:1}
        prefix_sum = 0
        res = 0
            
        for r in range(len(nums)):
            prefix_sum += nums[r]

            if prefix_sum - k in cnt:
                res += cnt[prefix_sum - k]
            
            if prefix_sum not in cnt:
                cnt[prefix_sum] = 1
            else:
                cnt[prefix_sum] += 1
                

        return res
