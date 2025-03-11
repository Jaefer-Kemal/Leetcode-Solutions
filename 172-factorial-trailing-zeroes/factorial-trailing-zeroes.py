def factorial(num):
    if num == 0 or num == 1:
        return 1
    
    return num * factorial(num - 1)

class Solution:
    def trailingZeroes(self, n: int) -> int:
        x = factorial(n)
        
        count = 0 
        while x % 10 == 0:
            x = x // 10
            count += 1
        
        return count

