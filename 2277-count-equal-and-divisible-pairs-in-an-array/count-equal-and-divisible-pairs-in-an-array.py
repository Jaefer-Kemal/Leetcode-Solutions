class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        dic = {}
        l = 0
        while l < len(nums):
            if nums[l] not in  dic:
                dic[nums[l]] = [l]
            else:
                for value in dic[nums[l]]:
                    if (value * l) % k == 0:
                        count += 1
                dic[nums[l]].append(l)
            
            l += 1
        return count

        '''First Solution'''
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if i < len(nums):
        #             if nums[i] == nums[j] and (i * j) % k == 0:
        #                 count += 1
        
        # return count