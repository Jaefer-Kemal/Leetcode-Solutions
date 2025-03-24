class Solution:
    def mySqrt(self, x: int) -> int:

        def binarySearch(low, high, ans):
            if low > high:
                return ans
            
            mid = (low + high) // 2

            if mid * mid <= x:
                ans = mid
                return binarySearch(mid + 1,high, ans)
            
            else:
                return binarySearch(low,mid - 1, ans)

        
        return binarySearch(0, x, 0)