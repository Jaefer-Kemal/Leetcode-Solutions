class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX, INT_MIN = 2 ** 31 - 1, -2 ** 31
        
        sign = 1
        index = 0
        if x < 0:
            sign = -1
            index += 1
        
        x = abs(x)
        
        res = 0
        while x != 0:
            digit = x % 10
            res = res * 10 + digit
            x //= 10
            
        if res > (INT_MAX):
            return 0
        
        return res * sign
            