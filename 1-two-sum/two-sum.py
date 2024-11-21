class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        used = {}
        l = 0
        while l < len(nums):
            if nums[l] in used:
                return [l,used[nums[l]]]
            else:
                used[target - nums[l]] = l
            l += 1
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

                        
                
                        
                