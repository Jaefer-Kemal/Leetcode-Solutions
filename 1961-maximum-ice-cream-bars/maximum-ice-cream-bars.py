class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count_arr = [0] * (max(costs) + 1)
        maximum_ice_cream = 0

        for cost in costs:
            if cost <= coins:
                count_arr[cost] += 1
        
        for cost in range(len(count_arr)):
            while coins != 0 and count_arr[cost] > 0 and coins >= cost:
                maximum_ice_cream += 1
                coins -= cost
                count_arr[cost] -= 1
            
            if coins == 0:
                break
        
        return maximum_ice_cream
