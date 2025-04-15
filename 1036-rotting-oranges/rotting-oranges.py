class Solution:
    def isbound(self,n,m, row, col):
        return 0 <= row < n and 0 <= col < m

    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        queue = deque()

        fresh = 0
        for row in range(n):
            for col in range(m):
                orange = grid[row][col]

                if  orange == 2:
                    queue.append((row,col))   

                elif orange == 1:
                    fresh += 1
        
        min_time = 0

        while queue and fresh:
            len_ = len(queue)

            for _ in range(len_):
                row, col = queue.popleft()

                if self.isbound(n,m, row + 1,col) and grid[row + 1][col] == 1:
                    fresh -= 1
                    grid[row + 1][col] = 2
                    queue.append((row + 1,col))

                if self.isbound(n,m, row, col + 1) and grid[row][col + 1] == 1:
                    fresh -= 1
                    grid[row][col + 1] = 2
                    queue.append((row, col + 1))

                if self.isbound(n,m, row - 1,col) and grid[row - 1][col] == 1:
                    fresh -= 1
                    grid[row - 1][col] = 2
                    queue.append((row - 1,col))

                if self.isbound(n,m, row,col - 1) and grid[row][col - 1] == 1:
                    fresh -= 1
                    grid[row][col - 1] = 2
                    queue.append((row, col - 1))

            min_time += 1

        if fresh:
            print(fresh)
            return -1

        return min_time

                


