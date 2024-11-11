class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        reverse = 0
        temp = x

        while temp > 0 :
            remainder = temp % 10
            reverse = (reverse *  10) + remainder
            temp = temp // 10

        if reverse == x:
            return True
        return False

        # l = 0
        # x = str(x)
        # r = len(x) - 1
        # while l < r:
        #     if x[l] != x[r]:
        #         return False
        #     l += 1
        #     r -= 1
        # return True 
        