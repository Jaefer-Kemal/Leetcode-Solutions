class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = [1] * (n + 1)
        suffix_product = [1] * (n + 1)

        for i in range(1, n + 1):
            prefix_product[i] = nums[i - 1] * prefix_product[i - 1]
            suffix_product[i] = nums[-(i)] * suffix_product[i - 1]


        results = [0] * n
        for i in range(n):
            results[i] = prefix_product[i] * suffix_product[-(i + 2)]
        
        return results
