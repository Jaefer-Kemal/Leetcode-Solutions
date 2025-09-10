class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        monotonic_stack = []
        maximum_profit = 0
        for price in prices:
            
            while monotonic_stack and monotonic_stack[-1] > price:
                num = monotonic_stack.pop()
                if monotonic_stack:
                    maximum_profit = max(maximum_profit, num - monotonic_stack[0])        

            monotonic_stack.append(price)
        
        if monotonic_stack and len(monotonic_stack) >= 2:
            maximum_profit = max(maximum_profit, monotonic_stack[-1] - monotonic_stack[0])

        return maximum_profit

        