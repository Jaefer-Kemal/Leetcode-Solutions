class Solution:
    def bounded(self, row, col, row_i, col_i, n, m):
        return 0 <= row + row_i < n and 0 <= col + col_i < m

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_sum = 0
        visited = [[False] * m for _ in range(n)]

        graphs = defaultdict(list)

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 0:
                    continue
                
                graphs[(row,col)].append((row,col))

                if self.bounded(row,col,1,0,n, m) and grid[row + 1][col] != 0:
                    graphs[(row,col)].append((row + 1,col))

                if self.bounded(row,col,0,1,n, m) and grid[row][col + 1] != 0:
                    graphs[(row,col)].append((row,col + 1))

                if self.bounded(row,col,-1,0,n, m) and grid[row - 1][col] != 0:
                    graphs[(row,col)].append((row - 1,col))

                if self.bounded(row,col,0,-1,n, m) and grid[row][col - 1] != 0:
                    graphs[(row,col)].append((row,col - 1))

        for portion in graphs:
            stack = [portion]
            current_sum = 0

            while stack:
                row, col = stack.pop()

                if visited[row][col]:
                    continue
                
                visited[row][col] = True

                current_sum += grid[row][col]
                neighbour = graphs[(row, col)]

                if len(neighbour) == 1:
                    continue

                for node in neighbour:
                    stack.append(node)

            max_sum = max(max_sum, current_sum)

        return max_sum