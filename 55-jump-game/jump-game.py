class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        r = len(nums) - 1
        l = r - 1
        
        make_it = True

        while l >= 0:
            if l + nums[l] >= r:
                make_it = True
                r = l
                l -= 1
            else:
                make_it = False
                l -= 1
        
        if make_it:
            return True

        return False
                

        