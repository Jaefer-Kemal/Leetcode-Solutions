class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums) + 1)
        suffix = [0] * (len(nums) + 1)
        suffix[-1] = 1
        ans = []
        for i in range(1,len(nums) + 1):
            prefix[i] = nums[i - 1] * prefix[i-1] 
            
            suffix[-(i+1)] = nums[-i] * suffix[-(i)]
            
        for i in range(len(nums)):
            ans.append(prefix[i] * suffix[i + 1])
        
        return ans