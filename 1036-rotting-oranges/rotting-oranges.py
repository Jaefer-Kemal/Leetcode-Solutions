class Solution:
    def isbound(self, n, m, row, col):
        return 0 <= row < n and 0 <= col < m

    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        direction = ((0,1),(1,0),(-1,0),(0,-1))
        queue = deque()
        min_time = 0
        fresh = 0

        for row in range(n):
            for col in range(m):
                orange = grid[row][col]

                if  orange == 2:
                    queue.append((row,col))   

                elif orange == 1:
                    fresh += 1
        

        while queue and fresh:
            len_ = len(queue)

            for _ in range(len_):
                row, col = queue.popleft()

                for nr, nc in direction:
                    if self.isbound(n, m, row + nr, col + nc) and grid[row + nr][col + nc] == 1:
                        fresh -= 1
                        grid[row + nr][col + nc] = 2
                        queue.append((row + nr, col + nc))

            min_time += 1

        if fresh:
            return -1

        return min_time

                


