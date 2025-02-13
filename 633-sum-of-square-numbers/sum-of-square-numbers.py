class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low = 0
        high = int(sqrt(c))+1

        while low <= high:
            res = (low * low) + (high * high)

            if res == c:
                return True

            elif res > c:
                high -= 1
                
            else:
                low += 1

        return False
        