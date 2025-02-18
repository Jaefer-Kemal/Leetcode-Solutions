class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_pro = [1] * (n + 1)
        suffix_pro = [1] * (n + 1)

        for i in range(1, n + 1):
            prefix_pro[i] = nums[i - 1] * prefix_pro[i - 1]
            suffix_pro[i] = nums[-(i)] * suffix_pro[i - 1]


        results = [0] * n
        for i in range(n):
            results[i] = prefix_pro[i] * suffix_pro[-(i + 2)]
        
        return results
