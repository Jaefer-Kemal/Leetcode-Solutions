class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high

        def isValid(speed):
            current_hour = 0

            for pile in piles:
                current_hour += ceil(pile / speed)
            
            return current_hour <= h


        while low <= high:
            mid = (low + high) // 2

            if isValid(mid):
                high = mid - 1
                ans = mid
            else:
                low = mid + 1

        return ans