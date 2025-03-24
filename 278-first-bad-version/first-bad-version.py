# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        def binarySearch(low, high, ans):
            if low > high:
                return ans
            
            mid = (low + high) // 2

            if isBadVersion(mid):
                ans = mid
                return binarySearch(low ,mid - 1, ans)

            else:
                return binarySearch(mid + 1,high, ans)

        
        return binarySearch(1, n, n)