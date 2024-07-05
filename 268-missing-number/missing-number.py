class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        len_ = len(nums)
        dic = {}
        for i in range(0,len_+1):
                dic[i]=0
        
        for num in nums:
            if num in dic:
                dic[num]+=1
        
        for key,value in dic.items():
            if value==0:
                return key
        