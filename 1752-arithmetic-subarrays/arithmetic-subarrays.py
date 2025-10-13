class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for query in zip(l,r):
            left = query[0]
            right = query[1]
            isArithmetic  = True
            sorted_nums = sorted(nums[left: right + 1])
            d = sorted_nums[1] - sorted_nums[0]

            for i in range(0, len(sorted_nums) - 1):
                if d != sorted_nums[i + 1] - sorted_nums[i]:
                    isArithmetic = False
                    break
            
            res.append(isArithmetic)

        return res
