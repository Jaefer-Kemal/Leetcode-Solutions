class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)//2
        for row in range(len(matrix)):
            for col in range(row + 1, len(matrix[0])):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
                
        for row in range(len(matrix)):
            matrix[row].reverse()
                
                
                    
        