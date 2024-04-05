class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        page=[]
        
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                    continue
            l,r=1+i,len(nums)-1
            while l<r:
                cumsum=nums[i]+nums[l]+nums[r]
                if cumsum>0:
                    r-=1
                elif cumsum<0:
                    l+=1
                else:
                    page.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return page
                        
                    
                
            