class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_mod_count = defaultdict(int)
        prefix_mod_count[0] = 1

        prefix_sum = 0
        result = 0
        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            
            if mod in prefix_mod_count:
                result += prefix_mod_count[mod]
            prefix_mod_count[mod] += 1

        return result