class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cnt = {0:1}
        res = 0
        prefix_sum = 0
        for r in range(len(nums)):
            prefix_sum += nums[r]
            rem = prefix_sum % k

            if rem in cnt:
                res += cnt[rem]
                cnt[rem] += 1
            
            else:
                cnt[rem] = 1

        return res
        