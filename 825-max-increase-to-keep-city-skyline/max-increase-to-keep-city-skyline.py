class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)

        row_dict = defaultdict(int)
        col_dict = defaultdict(int)
        
        max_sum = 0
        
        i = 0
        for row in grid:
            row_dict[i] = max(row)
            i += 1

        for col in range(n):
            maxim = 0
            for row in range(n):
                maxim = max(maxim, grid[row][col])
            
            col_dict[col] = maxim

        
        for row in range(n):
            for col in range(n):
                max_sum += min(row_dict[row], col_dict[col]) - grid[row][col]

        return max_sum

