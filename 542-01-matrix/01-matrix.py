class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        result = [[-1] * m for _ in range(n)]
        queue = deque()

        # Step 1: Add all 0s to the queue and initialize their distance to 0
        for row in range(n):
            for col in range(m):
                if mat[row][col] == 0:
                    result[row][col] = 0
                    queue.append((row, col))
        
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        # Step 2: BFS from all 0s simultaneously
        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < n and 0 <= nc < m and result[nr][nc] == -1:
                    result[nr][nc] = result[row][col] + 1
                    queue.append((nr, nc))
        
        return result
