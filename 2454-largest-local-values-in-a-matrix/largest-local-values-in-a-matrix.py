class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)-2
        m=[[0]*(n) for _ in range(n)]

        for i in range(n):
            for j in range(n):
                large=m[i][j]
                for row in range(i,i+3):
                    for col in range(j,j+3):
                        large=max(large,grid[row][col])
                m[i][j]=large
                
        return m
                    

                

        