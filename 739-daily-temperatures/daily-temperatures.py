class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * (len(temperatures))

        monotonic_stack = []
        
        for current_idx, temp in enumerate(temperatures):

            while monotonic_stack and monotonic_stack[-1][1] < temp:
                popped_idx = monotonic_stack.pop()[0]
                ans[popped_idx] = (current_idx - popped_idx)

            monotonic_stack.append([current_idx,temp])
        
        return ans