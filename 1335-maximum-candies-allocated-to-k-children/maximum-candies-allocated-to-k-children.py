class Solution:
    def checker(self, candies, mid):
        cnt = 0
        for candy in candies:
            cnt += floor(candy/mid)
        
        return cnt


    def maximumCandies(self, candies: List[int], k: int) -> int:
        total_candies = sum(candies)

        if total_candies < k:
            return 0

        low = 1
        high = max(candies)
        res = 0

        while low <= high:
            mid = (low + high) // 2

            if self.checker(candies, mid) >= k:
                res = mid
                low = mid + 1
            
            else:
                high = mid - 1
        
        return res