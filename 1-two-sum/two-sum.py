class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        used = {}
        for i in range(len(nums)):
            if target - nums[i] in used:
                return [i,used.get(target-nums[i])]
            else:
                used[nums[i]] = i
                
'''First Solution'''
#         l = 0
#         r = len(nums) - 1
#         dict_num = {}
#         for i, v in enumerate(nums):
#             dict_num[i] = int(v)
        
#         dict_num = sorted(dict_num.items(), key = lambda x:x[1])


#         while l < r:
#             sum_ =  dict_num[l][1] + dict_num[r][1]

#             if sum_ == target:
#                 return( [dict_num[l][0],dict_num[r][0]] )
            
#             elif sum_ > target:
#                 r -= 1
                
#             else:
#                 l += 1

                        
                
                        
                