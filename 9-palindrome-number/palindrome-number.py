class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        test = x
        res = 0
    
        while x:
            last_digit = x % 10
            res = last_digit + (res * 10)
            x = x // 10
        

        return res == test

