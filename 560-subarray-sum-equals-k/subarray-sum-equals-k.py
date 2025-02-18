class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        
        cnt = defaultdict(int)
        # Initialize it with 0 having frequency of 1, 
        # this helpful when prefix sum  equal k
        cnt[0] = 1

        result = 0
        n = len(nums)

        for r in range(n):
            prefix_sum += nums[r]

            # If (prefix_sum - k) is in cnt, it means there's a subarray 
            # ending at the current index that sums to k. Add its count to result.

            if (prefix_sum - k) in cnt:
                result += cnt[prefix_sum - k] 
                
            cnt[prefix_sum] += 1

        return result