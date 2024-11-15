class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        dic = {}
        array_left = []
        array_right = []
        for i in range(-1, len(nums)):
            if i == -1:
                numleft = 0
                array_left.append([numleft,i+1])
                continue
            if nums[i] == 0:
                numleft += 1
            array_left.append([numleft, i+1])

            
        for i in range(len(nums) , -1, -1):
            if i == len(nums):
                numright = 0
                array_right.append([numright, i])
                continue
            if nums[i] == 1:
                numright += 1
            array_right.append([numright, i])
        array_right.reverse()

        for i in range(len(array_right)):
            sum_ = array_right[i][0] + array_left[i][0]

            if sum_ not in dic:
                dic[sum_] = [i]
            else:
                dic[sum_].append(i)

        max_ = max(dic.keys())
        return dic[max_]

            








        '''Time Complexity'''
        # dic = {}

        # for i in range(len(nums) + 1):
        #     num_left = nums[:i].count(0)
        #     num_right = nums[i:].count(1)
        #     sum_ = num_left + num_right
        #     if sum_ not in dic:
        #         dic[sum_] = [i]
        #     else:
        #         dic[sum_].append(i)

        # max_ = max(dic.keys())
        # return dic[max_]