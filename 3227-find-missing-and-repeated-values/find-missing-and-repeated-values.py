class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        nums_count = defaultdict(int)
        ans = [None, None]
        n = len(grid) ** 2

        for arr in grid:
            for num in arr:
                nums_count[num] += 1
            

        for num in range(1, n + 1):
            if nums_count[num] == 2:
                ans[0] = num
            
            if nums_count[num] == 0:
                ans[1] = num
        
        return ans