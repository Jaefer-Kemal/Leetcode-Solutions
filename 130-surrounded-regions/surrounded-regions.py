class Solution:
    def inbound(self, row, col, n, m):
        return 0 <= row < n and 0 <= col < m

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = [[False] * m for _ in range(n)]

        def dfs(row, col, cells):
            visited[row][col] = True
            cells.append((row, col))
            is_border = row == 0 or col == 0 or row == n - 1 or col == m - 1

            for nr, nc in directions:
                if (self.inbound(row + nr, col + nc, n, m) 
                    and not visited[row + nr][col + nc]  
                    and board[row + nr][col + nc] == "O"):

                    result = dfs(row + nr, col + nc, cells)
                    is_border = is_border or result

            return is_border
        
        for row in range(n):
            for col in range(m):
                if not visited[row][col] and board[row][col] == "O":
                    cells = []
                    touches_board = dfs(row, col, cells)

                    if not touches_board:
                        for r, c in cells:
                            board[r][c] = "X"
        
        


        