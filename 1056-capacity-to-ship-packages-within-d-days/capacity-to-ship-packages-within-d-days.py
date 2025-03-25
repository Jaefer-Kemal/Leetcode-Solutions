class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        ans = high
        
        while low <= high:
            mid = (low + high) // 2

            possible_days = 1
            current_capacity = 0
            for w in weights:

                if current_capacity + w <= mid:
                    current_capacity += w
                else:
                    possible_days += 1
                    current_capacity = w
            
            if possible_days <= days:
                ans = mid
                high = mid - 1

            else:
                low = mid + 1

        
        return ans
                   
    


        