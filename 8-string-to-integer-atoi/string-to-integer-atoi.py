class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX , INT_MIN = 2**31 -1 , -2 ** 31 
        s = s.lstrip()
        sign = 1
        index = 0
        if not s:
            return 0
        if s[index] == "-":
            sign = -1
            index += 1
        elif s[index] == "+":
            index += 1
        result = 0
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result  * 10 + digit
            index += 1
        return sign * result