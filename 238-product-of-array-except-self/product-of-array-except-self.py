class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1]
        suffix_product = [1]

        for i in range(len(nums)):
            prefix_product.append(prefix_product[-1] * nums[i])
            suffix_product.append(suffix_product[-1] * nums[-(i+1)])
        
        result = [0] * len(nums)
        for i in range(len(result)):
            result[i] = suffix_product[-(i+2)] * prefix_product[i]
            
        return result