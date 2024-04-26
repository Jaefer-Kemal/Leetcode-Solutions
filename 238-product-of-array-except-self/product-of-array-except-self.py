class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix_pro = [1] * n
        suffix_pro = [1] * n

        prefix = 1
        suffix = 1

        for i in range(n):
            prefix_pro[i] = prefix
            prefix *= nums[i]     

            suffix_pro[-(i+1)] = suffix
            suffix *= nums[-(i+1)]
        
        res=[]
        for i in range(n):
            res.append(suffix_pro[i]*prefix_pro[i])
    

        return res
         
                
         
                